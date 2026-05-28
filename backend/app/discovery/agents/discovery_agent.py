import json
import os

from dotenv import load_dotenv

from openai import OpenAI

from app.discovery.prompts.discovery_prompts import (

    DISCOVERY_SYSTEM_PROMPT,

    DISCOVERY_QUESTION_PROMPTS,

    CONTEXT_EXTRACTION_PROMPT,
)

# =========================================
# LOAD ENV
# =========================================

load_dotenv()

# =========================================
# OPENAI CLIENT
# =========================================

client = OpenAI(

    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


class DiscoveryAgent:

    # =====================================
    # GENERATE QUESTION
    # =====================================

    @staticmethod
    def generate_question(

        step: str,

        context: dict,
    ):

        prompt = (
            DISCOVERY_QUESTION_PROMPTS
            .get(step)
        )

        response = client.chat.completions.create(

            model="gpt-4o-mini",

            messages=[

                {
                    "role": "system",

                    "content":
                        DISCOVERY_SYSTEM_PROMPT,
                },

                {
                    "role": "user",

                    "content":
                        f"""

                        Current Context:

                        {context}

                        Discovery Step:

                        {step}

                        Instructions:

                        {prompt}

                        Generate the next
                        intelligent discovery
                        question.

                        """
                },
            ],
        )

        return (

            response
            .choices[0]
            .message.content
        )

    # =====================================
    # EXTRACT STRUCTURED CONTEXT
    # =====================================

    @staticmethod
    def extract_structured_context(
        conversation: str
    ):

        response = client.chat.completions.create(

            model="gpt-4o-mini",

            response_format={
                "type": "json_object"
            },

            messages=[

                {
                    "role": "system",

                    "content":
                        CONTEXT_EXTRACTION_PROMPT,
                },

                {
                    "role": "user",

                    "content":
                        conversation,
                },
            ],
        )

        content = (

            response
            .choices[0]
            .message.content
        )

        try:

            return json.loads(
                content
            )

        except Exception:

            return {

                "error":
                    "Failed to parse AI response",

                "raw_response":
                    content,
            }