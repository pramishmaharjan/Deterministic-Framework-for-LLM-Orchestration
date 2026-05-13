import os
import json
from pathlib import Path
from core.brain_manager import BrainManager

def survey_memory(brain_root: Path):
    """
    Scans the memory directory to identify new knowledge clusters.
    A cluster is defined as a subdirectory containing information.
    """
    print("[Evolve] Surveying memory for new knowledge clusters...")
    memory_path = brain_root / "memory"
    clusters = {}

    if not memory_path.exists():
        return clusters

    for item in memory_path.iterdir():
        if item.is_dir():
            # The folder name is treated as the domain name
            clusters[item.name] = {
                "path": str(item),
                "type": "domain"
            }

    return clusters

def translate_to_routes(clusters, current_graph):
    """
    Maps discovered clusters to routing paths in the graph.
    Ensures Sovereign routes are not overwritten.
    """
    print("[Evolve] Translating clusters to deterministic routes...")
    updated_routes = current_graph.get("routes", {})

    for domain, info in clusters.items():
        # Check if this domain already has a route
        # We use a simplified mapping: Domain name becomes a specific route key
        # In a real scenario, we would use an LLM to map domain -> node sequence
        if domain not in updated_routes:
            print(f"[Evolve] New domain detected: {domain}. Generating route...")

            # Default growth pattern: Map new domains to a standard L3-like pipeline
            # but name the route after the domain
            updated_routes[domain] = ["ExtractionNode", "CleaningNode", "VerificationNode"]

    return updated_routes

def evolve_brain(graph_path: str, brain_root_str: str):
    """
    The main evolution cycle: Survey -> Translate -> Update.
    """
    graph_path = Path(graph_path)
    brain_root = Path(brain_root_str)

    # 1. Load current graph
    graph = {}
    if graph_path.exists():
        with open(graph_path, 'r') as f:
            graph = json.load(f)

    # 2. Survey and Translate
    clusters = survey_memory(brain_root)
    new_routes = translate_to_routes(clusters, graph)

    # 3. Update graph if changes occurred
    if new_routes != graph.get("routes", {}):
        print("[Evolve] Graph evolution detected. Updating graph.json...")
        graph["routes"] = new_routes
        with open(graph_path, 'w') as f:
            json.dump(graph, f, indent=4)
        return True

    print("[Evolve] No new growth detected. Graph remains stable.")
    return False

if __name__ == "__main__":
    # Simple standalone test
    root = BrainManager.get_brain_root()
    evolve_brain("config/graph.json", root)
