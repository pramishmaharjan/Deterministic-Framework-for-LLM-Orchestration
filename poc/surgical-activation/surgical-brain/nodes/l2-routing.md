# SOP: L2 - Operational Index

## Purpose
Map a user query to a deterministic path within the Brain's knowledge graph.

## Execution Protocol
1. **Graph Query**: Open `surgical-brain/graph.json`.
2. **Path Identification**: Locate the `route` or `node` that matches the intent of the query.
3. **Sequence Mapping**: Identify the linear sequence of nodes required to solve the task.
4. **Surgical Read**: Begin reading the nodes in the sequence.

## Failure Condition
If no matching route exists in `graph.json` $\to$ **Escalate to L4** for a custom graph synthesis.
