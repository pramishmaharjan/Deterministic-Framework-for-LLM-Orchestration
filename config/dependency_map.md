# Surgical Dependency Map (GitHub Registry)

This registry maps the Surgical Brain's functional nodes to their official source implementations.

| Tool Node | Official GitHub Repository | Surgical SOP |
| :--- | :--- | :--- |
| **langstruct** | `https://github.com/stanfordnlp/dspy` | Use for prompt optimization and type-safe schema design. |
| **langextract** | `[Link to official repo]` | Use for grounded, character-interval extraction. |
| **Polars** | `https://github.com/pola-rs/polars` | Use for high-performance, deterministic data cleaning. |
| **sqlglot** | `https://github.com/tobyji/sqlglot` | Use for cross-dialect SQL transpilation. |
| **sqlfluff** | `https://github.com/sqlfluff/sqlfluff` | Use for deterministic SQL linting and verification. |
| **ruflo** | `[Link to official repo]` | Use for multi-agent swarm orchestration. |
| **graphify** | `https://github.com/safishamsi/graphify` | Use for building the knowledge graph and routing map. |

**Execution Rule**: When a route identifies one of these tools, the agent must verify the current implementation against the official GitHub source to ensure the "Surgical" standard is met.
