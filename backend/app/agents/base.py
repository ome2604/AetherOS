from abc import ABC, abstractmethod

from app.orchestrator.state import WorkflowState


class BaseAgent(ABC):

    @abstractmethod
    def run(self, state: WorkflowState) -> WorkflowState:
        pass