from typing import Any, Dict, List, Optional
from pathlib import Path
import json

class RouteMissException(Exception):
    """Raised when the Router cannot find a valid path for the given query."""
    pass

class Router:
    """
    Deterministic Router implementing the 4-Tier Escalation Ladder.
    L1: Surgical-Lite -> L2: Operational Index -> L3: Functional Nodes -> L4: Orchestrated.
    """
    def __init__(self, graph_path: str = "config/graph.json"):
        self.graph_path = Path(graph_path)
        self.graph = self._load_graph()

    def _load_graph(self) -> Dict:
        if self.graph_path.exists():
            with open(self.graph_path, 'r') as f:
                return json.load(f)
        return {"routes": {}}

    def classify(self, query: str) -> str:
        query_lower = query.lower()
        if any(word in query_lower for word in ["what is", "define", "quick check"]):
            return "L1"
        if any(word in query_lower for word in ["find route", "map", "where is"]):
            return "L2"
        if any(word in query_lower for word in ["clean", "extract", "sql", "lint"]):
            return "L3"
        return "L4"

    def get_route(self, query: str) -> List[str]:
        tier = self.classify(query)
        print(f"[Router] Request classified as {tier}")

        # Query the dynamic graph instead of hardcoded dict
        routes = self.graph.get("routes", {})
        route = routes.get(tier)

        if not route:
            raise RouteMissException(f"No route found for tier {tier}")

        return route
