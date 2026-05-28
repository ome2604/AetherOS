import os

from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()

client = OpenAI(

    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


class BaseCopilot:

    def __init__(

        self,

        system_prompt: str,
    ):

        self.system_prompt = (
            system_prompt
        )

    def generate(

        self,

        context: str,
    ):

        response = (

            client.chat.completions.create(

                model="gpt-4o-mini",

                messages=[

                    {
                        "role": "system",

                        "content":
                            self.system_prompt,
                    },

                    {
                        "role": "user",

                        "content":
                            context,
                    },
                ],
            )
        )

        return (

            response
            .choices[0]
            .message.content
        )