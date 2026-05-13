# System Overview: The Escalation Ladder

The **Escalation Ladder** is the primary mechanism for managing "Cognitive Load" within the Surgical Brain OS.

## The Problem: Context Noise
When an LLM is given too much information (the "Everything-Bagel" prompt), it suffers from "Lost in the Middle" syndrome. It begins to ignore constraints and hallucinate details.

## The Solution: Tiered Activation
The ladder ensures a "Just-in-Time" (JIT) loading of context:

| Tier | Name | Trigger | Action | Memory Load |
| :--- | :--- | :--- | :--- | :--- |
| **L1** | Surgical-Lite | Trivial/Direct | Immediate Execution | Minimal |
| **L2** | Operational Index | Route-able Request | Query `graph.json` $\to$ Map Path | Low |
| **L3** | Functional Nodes | Tool-specific Need | Load Tool SOP $\to$ Execute | Medium |
| **L4** | Orchestrated | Complex Synthesis | Execute Pipeline $\to$ Sovereign Check | High |

## Execution Logic
1. **Analyze:** The `Router` classifies the query.
2. **Escalate:** If L1 cannot solve it, the system moves to L2.
3. **Route:** If L2 identifies a path, it triggers L3.
4. **Align:** Every L4 output is gated by the Sovereign State.
