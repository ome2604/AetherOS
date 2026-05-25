from app.orchestrator.state import WorkflowState

from app.agents.planner import PlannerAgent
from app.agents.executor import ExecutorAgent
from app.agents.reviewer import ReviewerAgent


planner_agent = PlannerAgent()
executor_agent = ExecutorAgent()
reviewer_agent = ReviewerAgent()


def planner_node(state: WorkflowState):

    return planner_agent.run(state)


def executor_node(state: WorkflowState):

    return executor_agent.run(state)


def reviewer_node(state: WorkflowState):

    return reviewer_agent.run(state)