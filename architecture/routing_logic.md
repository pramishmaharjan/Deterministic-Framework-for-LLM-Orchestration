# The Surgical Web: Deterministic Routing

Traditional AI agents "search" for information. The Surgical Web "routes" to it.

## Routing vs. Searching
- **Searching (Probabilistic):** "Find me something related to X." $\to$ Results in noisy, varied/unreliable output.
- **Routing (Deterministic):** "Follow the path: Node A $\to$ Node B $\to$ Node C." $\to$ Results in identical, predictable, and high-precision output.

## The Knowledge Graph (`graph.json`)
The system utilizes a Knowledge Graph to define the relationship between functional nodes. This graph is not just a list of tools, but a map of **dependencies**.

### Example: The "Surgical Data" Route
`Raw Text` $\to$ `ExtractionNode` $\to$ `CleaningNode` $\to$ `VerificationNode` $\to$ `SovereignAlignment`.

In this route:
- The **ExtractionNode** ensures no data is lost.
- The **CleaningNode** (Polars) ensures deterministic formatting.
- The **VerificationNode** (sqlglot) ensures the SQL is dialect-correct.
- The **SovereignAlignment** ensures the final report is professional.

If any node in this chain fails, the system does not "guess"—it triggers a routing error, preventing the delivery of a hallucinated result.
