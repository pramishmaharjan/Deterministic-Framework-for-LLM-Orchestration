import os
from core.router import Router
from core.sovereign import SovereignValidator
from core.orchestrator import Orchestrator
from nodes.data_nodes import LiteNode, IndexNode, ExtractionNode, CleaningNode, VerificationNode, SynthesisNode

def main():
    # 1. Initialize Core Engine
    router = Router()
    validator = SovereignValidator()
    orchestrator = Orchestrator(router, validator)

    # 2. Register Nodes (The Surgical Web)
    orchestrator.register_node("LiteNode", LiteNode("LiteNode", "L1"))
    orchestrator.register_node("IndexNode", IndexNode("IndexNode", "L2"))
    orchestrator.register_node("ExtractionNode", ExtractionNode("ExtractionNode", "L3"))
    orchestrator.register_node("CleaningNode", CleaningNode("CleaningNode", "L3"))
    orchestrator.register_node("VerificationNode", VerificationNode("VerificationNode", "L3"))
    orchestrator.register_node("SynthesisNode", SynthesisNode("SynthesisNode", "L4"))

    # 3. Test Different Tiers of the Escalation Ladder
    queries = [
        "What is the Surgical Brain?",                # Should trigger L1
        "Find the route to the data brain",           # Should trigger L2
        "Clean this CSV and convert to SQL",          # Should trigger L3
        "Convert a PDF to a verified SQL report"      # Should trigger L4
    ]

    for query in queries:
        result = orchestrator.run(query)
        print(f"\nFINAL RESULT:\n{result}\n")
        print("-" * 50)

if __name__ == "__main__":
    main()
