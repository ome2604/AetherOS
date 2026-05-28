DISCOVERY_STEPS = [

    "collect_goal",

    "collect_users",

    "collect_constraints",

    "collect_scale",

    "collect_integrations",

    "generate_context",
]


class DiscoveryStateMachine:

    @staticmethod
    def get_next_step(
        current_step: str
    ):

        try:

            index = (
                DISCOVERY_STEPS.index(
                    current_step
                )
            )

            return DISCOVERY_STEPS[
                index + 1
            ]

        except Exception:

            return "completed"