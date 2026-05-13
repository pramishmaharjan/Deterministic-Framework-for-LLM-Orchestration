from core.orchestrator import Orchestrator
from core.router import Router
from core.sovereign import SovereignValidator
from nodes.data_nodes import CleaningNode, ExtractionNode, VerificationNode
from core.brain_manager import BrainManager
from scripts.boot import boot_framework

def main():
    # 1. Boot Framework and Brain
    boot_framework()

    # 2. Initialize Core Components
    router = Router()
    validator = SovereignValidator()
    orchestrator = Orchestrator(router, validator)

    # 3. Register Functional Nodes
    orchestrator.register_node("ExtractionNode", ExtractionNode("extraction", "L3"))
    orchestrator.register_node("CleaningNode", CleaningNode("cleaning", "L3"))
    orchestrator.register_node("VerificationNode", VerificationNode("verification", "L3"))

    # 4. Run a Deterministic Query
    query = "Clean the user data from the recent CSV import and verify the schema."
    result = orchestrator.run(query)

    print(f"\nFinal Verified Output:\n{result}")

if __name__ == "__main__":
    main()
