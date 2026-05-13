from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseNode(ABC):
    """
    Abstract Base Class for all Surgical Brain functional nodes.
    Ensures a consistent interface for deterministic routing.
    """
    def __init__(self, name: str, stage: str):
        self.name = name
        self.stage = stage

    @abstractmethod
    def execute(self, input_data: Any, context: Dict[str, Any]) -> Any:
        """
        Execute the node's specific surgical operation.
        """
        pass
