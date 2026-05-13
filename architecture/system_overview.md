# System Overview: The Escalation Ladder

The core of the Surgical Brain OS is the **Escalation Ladder**. This prevents the AI from loading the entire "brain" for every prompt, which is the primary cause of token bloat and cognitive drift.

## The Logic Flow
1. **Analyze**: Classify the request complexity.
2. **L1 (Surgical-Lite)**: Can this be solved with a simple read or grep? If yes, finish.
3. **L2 (Operational Index)**: If L1 fails, load the `graph.json` and `MEMORY.md` to find the specific route to the answer.
4. **L3 (Functional Nodes)**: Once the route is found, perform a "Surgical Read" of the specific tool's SOP.
5. **L4 (Orchestrated)**: For complex synthesis, trigger the tool chain and align the result with the `Sovereign State`.

## Why this works
By treating the AI's context window as **RAM** and the Work Brain as a **Disk**, we only load the "pages" of memory required for the current operation. This ensures that the AI's "focus" is always 100% on the task at hand.
