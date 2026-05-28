from sqlalchemy.orm import Session

from app.langgraph.runtime import (
    LangGraphRuntime,
)

from app.langgraph.checkpoint import (
    GraphCheckpointManager,
)

from app.langgraph.recovery import (
    GraphRecoveryEngine,
)


class DurableLangGraphRuntime:

    def __init__(
        self,
        db: Session,
    ):

        self.db = db

        self.runtime = (
            LangGraphRuntime()
        )

    def execute(
        self,
        workflow_id: str,
        initial_state: dict,
    ):

        # =====================================
        # RECOVERY LOGIC
        # =====================================

        recovery = (
            GraphRecoveryEngine
            .recover_checkpoint(
                self.db,
                workflow_id,
            )
        )

        if recovery:

            print(
                f"\n[RECOVERY] "
                f"Recovered workflow: "
                f"{workflow_id}"
            )

            state = recovery[
                "workflow_state"
            ]

            current_node = (
                recovery["node_name"]
            )

        else:

            print(
                f"\n[NEW WORKFLOW] "
                f"Starting workflow: "
                f"{workflow_id}"
            )

            state = initial_state

            current_node = (
                state["current_node"]
            )

        # =====================================
        # EXECUTION LOOP
        # =====================================

        while current_node != "completed":

            print(
                f"\n[EXECUTING NODE] "
                f"{current_node}"
            )

            # =================================
            # EXECUTE CURRENT NODE
            # =================================

            state = (
                self.runtime.execute_node(
                    current_node,
                    state,
                )
            )

            # =================================
            # DETERMINE NEXT NODE
            # =================================

            next_node = (
                self.runtime.get_next_node(
                    state
                )
            )

            # =================================
            # UPDATE STATE
            # =================================

            state["current_node"] = (
                next_node
            )

            if next_node == "completed":

                state["status"] = (
                    "completed"
                )

            else:

                state["status"] = (
                    "running"
                )

            # =================================
            # SAVE CHECKPOINT
            # =================================

            print(
                f"[CHECKPOINT SAVED] "
                f"{next_node}"
            )

            GraphCheckpointManager.save_checkpoint(

                db=self.db,

                workflow_id=workflow_id,

                node_name=next_node,

                state=state,
            )

            # =================================
            # MOVE TO NEXT NODE
            # =================================

            current_node = next_node

        # =====================================
        # WORKFLOW COMPLETED
        # =====================================

        print(
            f"\n[WORKFLOW COMPLETED] "
            f"{workflow_id}"
        )

        return state