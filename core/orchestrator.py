from typing import Any, Dict, List
from pathlib import Path
from .brain_manager import BrainManager
from .router import Router, RouteMissException
from .sovereign import SovereignValidator
from nodes.data_nodes import (
    LiteNode, IndexNode, ExtractionNode, CleaningNode,
    VerificationNode, SynthesisNode, LangStructNode, LangExtractNode
)
from scripts.evolve import evolve_brain

NODE_REGISTRY = {
    "LiteNode": LiteNode,
    "IndexNode": IndexNode,
    "ExtractionNode": ExtractionNode,
    "CleaningNode": CleaningNode,
    "VerificationNode": VerificationNode,
    "SynthesisNode": SynthesisNode,
    "LangStructNode": LangStructNode,
    "LangExtractNode": LangExtractNode,
}

NODE_SOP_MAP = {
    "LangStructNode": Path("Lang/lang_struct/SOP.md"),
    "LangExtractNode": Path("Lang/lang_extract/SOP.md"),
    "ExtractionNode": Path("Lang/lang_extract/SOP.md"),
    "CleaningNode": Path("Lang/cleaning/SOP.md"),
    "VerificationNode": Path("Lang/verification/SOP.md"),
    "SynthesisNode": Path("Lang/synthesis/SOP.md"),
    "LiteNode": Path("Lang/lite/SOP.md"),
    "IndexNode": Path("Lang/index/SOP.md"),
}

class Orchestrator:
    def __init__(self, router: Router, validator: SovereignValidator):
        self.router = router
        self.validator = validator
        self.brain_root = BrainManager.get_brain_root()

    def load_node_surgically(self, node_name: str) -> str:
        rel_path = NODE_SOP_MAP.get(node_name)
        if rel_path is None:
            return f"No SOP mapping for {node_name}"
        sop_path = Path(self.brain_root) / rel_path
        if sop_path.exists():
            return sop_path.read_text(encoding="utf-8")
        return f"SOP not found at {sop_path}"

    def _ensure_synergy(self, route: List[str]) -> List[str]:
        if "LangStructNode" in route and "LangExtractNode" in route:
            si = route.index("LangStructNode")
            ei = route.index("LangExtractNode")
            if si > ei:
                route[si], route[ei] = route[ei], route[si]
        return route

    def run(self, query: str) -> str:
        print(f"\n[Surgical Brain] Analyzing request: {query}")

        try:
            route = self.router.get_route(query)
            tier = self.router.classify(query)
        except RouteMissException:
            print("[Orchestrator] Route miss detected. Triggering Brain Evolution...")
            if evolve_brain("config/graph.json", self.brain_root):
                print("[Orchestrator] Brain evolved. Re-attempting route...")
                self.router.graph_loader._graph = None
                route = self.router.get_route(query)
                tier = self.router.classify(query)
            else:
                return "Surgical Error: Request cannot be routed and no new knowledge was found to evolve the brain."

        if tier in ("L3", "L4"):
            route = self._ensure_synergy(route)

        print(f"[Surgical Brain] Route Selected: {' -> '.join(route)}")
        current_state = query
        for node_name in route:
            node_class = NODE_REGISTRY.get(node_name)
            if node_class is None:
                print(f"[Warning] Node class '{node_name}' not found in registry.")
                continue
            sop_content = self.load_node_surgically(node_name)
            node = node_class(name=node_name, stage=tier)
            context = {"brain_root": self.brain_root, "sop": sop_content}
            current_state = node.execute(current_state, context)

        return self.validator.validate(current_state)
