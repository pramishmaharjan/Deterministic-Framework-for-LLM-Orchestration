# The Surgical Web: Deterministic Routing

Traditional AI agents "search" for information. The Surgical Web "routes" to it.

## routing vs. Searching
- **Searching**: "Find me something related to X." (Probabilistic, noisy).
- **Routing**: "Follow the path: Node A $\to$ Node B $\to$ Node C." (Deterministic, precise).

## The Spider Web Implementation
The architecture uses a `graph.json` file generated via `graphify` to map relationships between tools and concepts.

### Example Routing Path:
`Raw Text` $\to$ `Extraction Node` $\to$ `Cleaning Node (Polars)` $\to$ `Verification Node (sqlfluff)` $\to$ `Synthesis Node (ruflo)` $\to$ `Sovereign Alignment`.

## The Sovereign State
The final node in every high-complexity route is the **Sovereign State**. This is a document containing the "Core Values" and "Technical Constraints" of the system. No output is delivered to the user until it has been validated against the Sovereign State.
