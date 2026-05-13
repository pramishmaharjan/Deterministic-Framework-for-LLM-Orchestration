from typing import Any, Dict, List
import os
from .router import Router
from .sovereign import SovereignValidator

class Orchestrator:
    """
    The core execution engine of the Surgical Brain OS.
    """
    def __init__(self, router: Router, validator: SovereignValidator):
        self.router = router
        self.validator = validator
        self.nodes = {}
        self.brain_root = os.getenv("BRAIN_ROOT_PATH", "C:/SurgicalBrain/Work")

    def register_node(self, name: str, node_instance: Any):
        self.nodes[name] = node_instance

    def run(self, query: str) -> str:
        print(f"\n[Surgical Brain] Analyzing request: {query}")
        route = self.router.get_route(query)
        print(f"[Surgical Brain] Route Selected: {' -> '.join(route)}")
        current_state = query
        for node_name in route:
            if node_name in self.nodes:
                node = self.nodes[node_name]
                context = {"brain_root": self.brain_root}
                current_state = node.execute(current_state, context)
            else:
                print(f"[Warning] Node '{node_name}' not registered.")
        return self.validator.validate(current_state)
