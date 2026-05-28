import asyncio

from sqlalchemy.orm import Session

from app.discovery.repositories.discovery_repository import (
    DiscoveryRepository,
)

from app.discovery.state.discovery_state import (
    DiscoveryStateMachine,
)

from app.discovery.agents.discovery_agent import (
    DiscoveryAgent,
)

from app.discovery.realtime.discovery_ws_manager import (
    discovery_ws_manager,
)

from app.models.discovery_message import (
    DiscoveryMessage,
)


class DiscoveryService:

    # =====================================
    # START DISCOVERY
    # =====================================

    @staticmethod
    def start_discovery(

        db: Session,

        title: str,

        initial_input: str,
    ):

        # =================================
        # CREATE SESSION
        # =================================

        session = (

            DiscoveryRepository
            .create_session(

                db=db,

                title=title,
            )
        )

        # =================================
        # SAVE USER MESSAGE
        # =================================

        DiscoveryRepository.save_message(

            db=db,

            session_id=session.id,

            role="user",

            content=initial_input,
        )

        # =================================
        # INITIAL CONTEXT
        # =================================

        extracted_context = {

            "goal": initial_input
        }

        current_step = (
            session.current_step
        )

        # =================================
        # GENERATE AI QUESTION
        # =================================

        ai_response = (

            DiscoveryAgent
            .generate_question(

                step=current_step,

                context=(
                    extracted_context
                ),
            )
        )

        # =================================
        # SAVE AI RESPONSE
        # =================================

        DiscoveryRepository.save_message(

            db=db,

            session_id=session.id,

            role="assistant",

            content=ai_response,
        )

        # =================================
        # UPDATE SESSION
        # =================================

        session.extracted_context = (
            extracted_context
        )

        DiscoveryRepository.update_session(

            db=db,

            session=session,
        )

        # =================================
        # BROADCAST EVENT
        # =================================

        try:

            loop = asyncio.get_running_loop()

            loop.create_task(

                discovery_ws_manager.broadcast(

                    session_id=str(session.id),

                    message={

                        "event":
                            "discovery_started",

                        "session_id":
                            str(session.id),

                        "ai_response":
                            ai_response,

                        "step":
                            current_step,
                    },
                )
            )

        except Exception:

            pass

        # =================================
        # RESPONSE
        # =================================

        return {

            "session_id":
                str(session.id),

            "current_step":
                session.current_step,

            "ai_response":
                ai_response,

            "extracted_context":
                extracted_context,
        }

    # =====================================
    # PROCESS MESSAGE
    # =====================================

    @staticmethod
    def process_message(

        db: Session,

        session_id: str,

        message: str,
    ):

        # =================================
        # LOAD SESSION
        # =================================

        session = (

            DiscoveryRepository
            .get_session(

                db=db,

                session_id=session_id,
            )
        )

        if not session:

            raise Exception(
                "Discovery session not found"
            )

        current_step = (
            session.current_step
        )

        # =================================
        # SAVE USER MESSAGE
        # =================================

        DiscoveryRepository.save_message(

            db=db,

            session_id=session_id,

            role="user",

            content=message,
        )

        # =================================
        # REALTIME USER EVENT
        # =================================

        try:

            loop = asyncio.get_running_loop()

            loop.create_task(

                discovery_ws_manager.broadcast(

                    session_id=session_id,

                    message={

                        "event":
                            "user_message",

                        "message":
                            message,

                        "step":
                            current_step,
                    },
                )
            )

        except Exception:

            pass

        extracted_context = (
            session.extracted_context
            or {}
        )

        # =================================
        # CONTEXT EXTRACTION
        # =================================

        if current_step == "collect_goal":

            extracted_context[
                "goal"
            ] = message

        elif current_step == "collect_users":

            extracted_context[
                "users"
            ] = message

        elif current_step == "collect_constraints":

            extracted_context[
                "constraints"
            ] = message

        elif current_step == "collect_scale":

            extracted_context[
                "scale"
            ] = message

        elif current_step == "collect_integrations":

            extracted_context[
                "integrations"
            ] = message

        # =================================
        # NEXT STEP
        # =================================

        next_step = (

            DiscoveryStateMachine
            .get_next_step(
                current_step
            )
        )

        # =================================
        # UPDATE SESSION
        # =================================

        session.current_step = (
            next_step
        )

        session.extracted_context = (
            extracted_context
        )

        DiscoveryRepository.update_session(

            db=db,

            session=session,
        )

        # =================================
        # GENERATE AI RESPONSE
        # =================================

        if next_step == "completed":

            ai_response = (
                "Discovery completed."
            )

        else:

            ai_response = (

                DiscoveryAgent
                .generate_question(

                    step=next_step,

                    context=(
                        extracted_context
                    ),
                )
            )

        # =================================
        # SAVE AI RESPONSE
        # =================================

        DiscoveryRepository.save_message(

            db=db,

            session_id=session_id,

            role="assistant",

            content=ai_response,
        )

        # =================================
        # REALTIME AI EVENT
        # =================================

        try:

            loop = asyncio.get_running_loop()

            loop.create_task(

                discovery_ws_manager.broadcast(

                    session_id=session_id,

                    message={

                        "event":
                            "ai_response",

                        "message":
                            ai_response,

                        "step":
                            next_step,
                    },
                )
            )

        except Exception:

            pass

        # =================================
        # GENERATE INTELLIGENCE
        # =================================

        if next_step == "generate_context":

            messages = (

                db.query(
                    DiscoveryMessage
                )

                .filter(
                    DiscoveryMessage.session_id
                    == session_id
                )

                .all()
            )

            conversation = "\n".join([

                f"{m.role}: {m.content}"

                for m in messages
            ])

            intelligence = (

                DiscoveryAgent
                .extract_structured_context(
                    conversation
                )
            )

            DiscoveryRepository.create_project_context(

                db=db,

                session_id=session_id,

                project_name=session.title,

                structured_context=intelligence,
            )

            # =============================
            # REALTIME INTELLIGENCE EVENT
            # =============================

            try:

                loop = asyncio.get_running_loop()

                loop.create_task(

                    discovery_ws_manager.broadcast(

                        session_id=session_id,

                        message={

                            "event":
                                "intelligence_generated",

                            "intelligence":
                                intelligence,
                        },
                    )
                )

            except Exception:

                pass

        # =================================
        # RESPONSE
        # =================================

        return {

            "session_id":
                str(session.id),

            "current_step":
                next_step,

            "ai_response":
                ai_response,

            "extracted_context":
                extracted_context,
        }

    # =====================================
    # GENERATE PROJECT INTELLIGENCE
    # =====================================

    @staticmethod
    def generate_project_intelligence(

        db: Session,

        session_id: str,
    ):

        session = (

            DiscoveryRepository
            .get_session(

                db=db,

                session_id=session_id,
            )
        )

        if not session:

            raise Exception(
                "Session not found"
            )

        # =================================
        # LOAD MESSAGES
        # =================================

        messages = (

            db.query(
                DiscoveryMessage
            )

            .filter(
                DiscoveryMessage.session_id
                == session_id
            )

            .all()
        )

        # =================================
        # BUILD CONVERSATION
        # =================================

        conversation = "\n".join([

            f"{m.role}: {m.content}"

            for m in messages
        ])

        # =================================
        # AI EXTRACTION
        # =================================

        intelligence = (

            DiscoveryAgent
            .extract_structured_context(
                conversation
            )
        )

        # =================================
        # SAVE CONTEXT
        # =================================

        DiscoveryRepository.create_project_context(

            db=db,

            session_id=session_id,

            project_name=session.title,

            structured_context=intelligence,
        )

        # =================================
        # REALTIME INTELLIGENCE EVENT
        # =================================

        try:

            loop = asyncio.get_running_loop()

            loop.create_task(

                discovery_ws_manager.broadcast(

                    session_id=session_id,

                    message={

                        "event":
                            "intelligence_generated",

                        "intelligence":
                            intelligence,
                    },
                )
            )

        except Exception:

            pass

        return intelligence