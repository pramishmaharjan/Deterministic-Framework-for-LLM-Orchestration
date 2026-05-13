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

    # 2. Populate Default Routing Graph (if missing)
    graph_file = config_dir / "graph.json"
    if not graph_file.exists():
        print("[Boot] Creating default routing graph...")
        sample_graph = {
            "version": "1.0",
            "routes": {
                "L1": ["LiteNode"],
                "L2": ["IndexNode", "LiteNode"],
                "L3": ["ExtractionNode", "CleaningNode", "VerificationNode"],
                "L4": ["ExtractionNode", "CleaningNode", "VerificationNode", "SynthesisNode"]
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
