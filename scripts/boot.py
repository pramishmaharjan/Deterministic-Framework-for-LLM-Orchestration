import os
import json
from pathlib import Path
from core.brain_manager import BrainManager

def boot_framework():
    """
    The 'Boot Sequence' for the Surgical Brain OS.
    Ensures that the local framework config and the external Brain data store
    are initialized before the orchestrator starts.
    """
    print("[Boot] Starting Surgical Brain Boot Sequence...")

    # 1. Ensure config directory exists
    config_dir = Path("config")
    config_dir.mkdir(parents=True, exist_ok=True)
    print(f"[Boot] Config directory verified: {config_dir}")

    # 2. Populate Default Routing Graph (if missing or outdated)
    graph_file = config_dir / "graph.json"
    needs_update = not graph_file.exists()

    if graph_file.exists():
        try:
            with open(graph_file, 'r') as f:
                current_graph = json.load(f)
                # Check if it's using the new Sovereign format (routes should be dicts, not lists)
                routes = current_graph.get("routes", {})
                if routes:
                    first_route = next(iter(routes.values()))
                    if not isinstance(first_route, dict):
                        needs_update = True
        except Exception:
            needs_update = True

    if needs_update:
        print("[Boot] Creating/Updating default routing graph to latest version...")
        sample_graph = {
            "version": "1.1",
            "routes": {
                "L1": {"path": ["LiteNode"], "sovereign": True},
                "L2": {"path": ["IndexNode", "LiteNode"], "sovereign": True},
                "L3": {"path": ["ExtractionNode", "CleaningNode", "VerificationNode"], "sovereign": False},
                "L4": {"path": ["ExtractionNode", "CleaningNode", "VerificationNode", "SynthesisNode"], "sovereign": False}
            },
            "description": "Deterministic mapping of request tiers to functional nodes."
        }
        with open(graph_file, 'w') as f:
            json.dump(sample_graph, f, indent=4)

    # 3. Populate Default Sovereign State (if missing)
    state_file = config_dir / "sovereign_state.md"
    if not state_file.exists():
        print("[Boot] Creating default sovereign state specification...")
        sample_state = (
            "# Sovereign State Specification\n\n"
            "## Core Constraints\n"
            "- Precision: No hallucinations; use only provided grounded data.\n"
            "- Factuality: All claims must be traceable to the source nodes.\n"
            "- Format: Technical, concise, and devoid of conversational filler.\n\n"
            "## Alignment Gate\n"
            "Output must be verified against the Deterministic routing path before delivery."
        )
        state_file.write_text(sample_state, encoding="utf-8")

    # 4. Initialize External Brain Structure
    print("[Boot] Initializing external Brain storage...")
    brain_root = BrainManager.initialize_brain_structure()
    print(f"[Boot] Brain successfully anchored at: {brain_root}")

    print("[Boot] System ready. Transitioning to Orchestration mode.\n")
    return brain_root

if __name__ == "__main__":
    boot_framework()
