from typing import Any, Dict, List
import os
from .brain_manager import BrainManager
from .router import Router, RouteMissException
from scripts.evolve import evolve_brain

class Orchestrator:
    """
    The core execution engine of the Surgical Brain OS.
    """
    def __init__(self, router: Router, validator: Any):
        self.router = router
        self.validator = validator
        self.nodes = {}
        self.brain_root = BrainManager.get_brain_root()

    def register_node(self, name: str, node_instance: Any):
        self.nodes[name] = node_instance

    def run(self, query: str) -> str:
        print(f"\n[Surgical Brain] Analyzing request: {query}")

        try:
            route = self.router.get_route(query)
        except RouteMissException:
            print("[Orchestrator] Route miss detected. Triggering Brain Evolution...")
            if evolve_brain("config/graph.json", self.brain_root):
                print("[Orchestrator] Brain evolved. Re-attempting route...")
                self.router.graph = self.router._load_graph()
                route = self.router.get_route(query)
            else:
                print("[Orchestrator] Evolution completed but no new route found.")
                return "Surgical Error: Request cannot be routed and no new knowledge was found to evolve the brain."

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
