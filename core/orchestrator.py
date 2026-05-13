from typing import Any, Dict, List
import os
from .router import Router
from .sovereign import SovereignValidator

class Orchestrator:
    """
    The core execution engine of the Surgical Brain OS.
    Coordinates the 4-Tier Escalation Ladder and ensures Sovereign alignment.
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

        # 1. Deterministic Routing (The Escalation Ladder)
        route = self.router.get_route(query)
        print(f"[Surgical Brain] Route Selected: {' -> '.join(route)}")

        # 2. Pipeline Execution
        current_state = query
        for node_name in route:
            if node_name in self.nodes:
                node = self.nodes[node_name]
                # Pass context including the brain root for node-specific disk access
                context = {"brain_root": self.brain_root}
                current_state = node.execute(current_state, context)
            else:
                print(f"[Warning] Route Node '{node_name}' not registered. Bypassing.")

        # 3. Sovereign State Alignment
        # The final output must pass through the sovereign validator
        final_output = self.validator.validate(current_state)

        return final_output
