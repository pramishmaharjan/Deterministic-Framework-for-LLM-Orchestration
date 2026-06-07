import re
from typing import Dict, Any
from .config import Surgical_Cores

class TriageEngine:
    """
    Deterministic router that maps user requests to L1-L4 tiers.
    No LLM used here to minimize tokens and latency.
    """

    PATTERNS = {
        "L1": [
            r"what is", r"read", r"find", r"where is", r"who is",
            r"show me", r"get", r"lookup"
        ],
        "L2": [
            r"how does", r"why", r"relationship", r"dependency",
            r"compare", r"difference", r"explain the link"
        ],
        "L3": [
            r"analyze", r"csv", r"metrics", r"stats", r"dataset",
            r"aggregate", r"calculate", r"trend", r"outlier"
        ],
        "L4": [
            r"implement", r"build", r"refactor", r"design", r"architect",
            r"create", r"develop", r"optimize", r"rewrite"
        ]
    }

    def route(self, request: str) -> Dict[str, Any]:
        request_lower = request.lower()

        # Priority check: L4 -> L3 -> L2 -> L1
        for tier in ["L4", "L3", "L2", "L1"]:
            for pattern in self.PATTERNS[tier]:
                if re.search(pattern, request_lower):
                    return self._build_route_response(tier)

        # Fallback to L2 if ambiguous, or L1 if very short
        return self._build_route_response("L2" if len(request) > 20 else "L1")

    def _build_route_response(self, tier: str) -> Dict[str, Any]:
        config = Surgical_Cores.get(tier, Surgical_Cores["L1"])
        return {
            "tier": tier,
            "effort": config["effort"],
            "model": config["model"],
            "description": f"Surgical {tier} routing activated."
        }

# Singleton instance
triage = TriageEngine()
