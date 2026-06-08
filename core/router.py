from typing import Any, Dict, List, Optional
from pathlib import Path
import json

class RouteMissException(Exception):
    """Raised when the Router cannot find a valid path for the given query."""
    pass

class LazyGraphLoader:
    """Handles on-demand loading of the routing graph to minimize memory overhead."""
    def __init__(self, path: Path):
        self.path = path
        self._graph = None

    def get_graph(self) -> Dict:
        if self._graph is None:
            if self.path.exists():
                with open(self.path, 'r') as f:
                    self._graph = json.load(f)
            else:
                self._graph = {"routes": {}}
        return self._graph

class Router:
    """
    Deterministic Router implementing the 4-Tier Escalation Ladder.
    L1: Surgical-Operational -> L2: Functional Nodes -> L3: Analytical -> L4: Orchestrated.
    """
    def __init__(self, graph_path: str = "config/graph.json"):
        self.graph_loader = LazyGraphLoader(Path(graph_path))

    def classify(self, query: str) -> str:
        query_lower = query.lower()
        graph = self.graph_loader.get_graph()
        routes = graph.get("routes", {})

        # 1. Check for dynamic domain matches from the graph
        for domain in routes.keys():
            if domain not in ["L1", "L2", "L3", "L4"]:
                normalized_domain = domain.replace("_", " ").lower()
                if normalized_domain in query_lower:
                    return domain

        # 2. Deterministic 4-Tier Escalation Ladder based on Brain OS
        # L1: Surgical-Operational (Simple lookups, basic edits, metadata)
        if any(word in query_lower for word in ["what is", "define", "quick check", "lookup", "metadata"]):
            return "L1"

        # L2: Functional Nodes (Targeted logic, index navigation, routing checks)
        if any(word in query_lower for word in ["find route", "map", "where is", "navigate", "index"]):
            return "L2"

        # L3: Analytical (Data transformation, extraction, SQL, linting, technical implementation)
        if any(word in query_lower for word in ["clean", "extract", "sql", "lint", "transform", "pipeline"]):
            return "L3"

        # L4: Orchestrated (High-complexity synthesis, swarm coordination, strategic planning)
        return "L4"

    def get_route(self, query: str) -> List[str]:
        tier = self.classify(query)
        print(f"[Router] Request classified as {tier}")

        graph = self.graph_loader.get_graph()
        routes = graph.get("routes", {})
        route_data = routes.get(tier)

        if not route_data:
            raise RouteMissException(f"No route found for tier {tier}")

        if isinstance(route_data, dict):
            return route_data.get("path", [])

        return route_data
