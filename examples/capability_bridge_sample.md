# Example: Capability Bridge (Routing Table)

This is a sample of how to map tools to a deterministic route.

## The "Surgical Data" Route
**Goal**: Convert a messy PDF into a verified SQL table.

| Step | Tool | Action | Output |
| :--- | :--- | :--- | :--- |
| 1 | `langextract` | Grounded Extraction | JSONL |
| 2 | `Polars` | Surgical Cleaning | Clean DataFrame |
| 3 | `sqlglot` | Dialect Routing | Target SQL |
| 4 | `sqlfluff` | Deterministic Linting | Sovereign SQL |
| 5 | `ruflo` | Swarm Synthesis | Verified Report |
