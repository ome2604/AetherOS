from abc import ABC, abstractmethod


class BaseTool(ABC):

    name: str

    description: str

    @abstractmethod
    def execute(self, input_data):

        pass