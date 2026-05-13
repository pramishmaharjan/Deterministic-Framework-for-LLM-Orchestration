from typing import Any, Dict, List
from .router import Router
from .sovereign import SovereignValidator

class Orchestrator:
    """
    Executes the determined route and ensures final Sovereign alignment.
    """
    def __init__(self, router: Router, validator: SovereignValidator):
        self.router = router
        self.validator = validator
        self.nodes = {}

    def register_node(self, name: str, node_instance: Any):
        self.nodes[name] = node_instance

    def run(self, query: str) -> str:
        print(f"\n[Orchestrator] Processing query: {query}")

        # 1. Route Determination
        route = self.router.get_route(query)
        print(f"[Orchestrator] Determined route: {' -> '.join(route)}")

        # 2. Sequential Execution
        current_data = query
        for node_name in route:
            if node_name in self.nodes:
                node = self.nodes[node_name]
                current_data = node.execute(current_data, {})
            else:
                print(f"[Warning] Node {node_name} not registered. Skipping.")

        # 3. Sovereign Alignment
        final_output = self.validator.validate(current_data)
        return final_output
