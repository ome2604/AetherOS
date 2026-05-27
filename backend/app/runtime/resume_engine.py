class ResumeEngine:

    @staticmethod
    def determine_resume_node(
        recovered_state: dict,
    ):

        node = recovered_state.get(
            "node_name"
        )

        if node == "planner":
            return "executor"

        if node == "executor":
            return "reviewer"

        if node == "reviewer":
            return "completed"

        return "planner"