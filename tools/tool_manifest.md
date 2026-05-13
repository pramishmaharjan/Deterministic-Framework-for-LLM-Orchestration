# The Surgical Suite: Tool Manifest

This registry maps the functional nodes of the Surgical Brain to their official industry-standard implementations.

## 1. Data Extraction & Structuring
| Node | Official Tool | Purpose |
| :--- | :--- | :--- |
| **ExtractionNode** | `langextract` | Grounded, character-interval extraction. |
| **SchemaNode** | `langstruct` | Type-safe schema design and prompt optimization. |

## 2. Data Manipulation & Routing
| Node | Official Tool | Purpose |
| :--- | :--- | :--- |
| **CleaningNode** | `Polars` | High-performance, memory-efficient deterministic cleaning. |
| **RoutingNode** | `sqlglot` | Cross-dialect SQL transpilation. |
| **VerificationNode** | `sqlfluff` | Deterministic SQL linting and verification. |

## 3. Orchestration & Synthesis
| Node | Official Tool | Purpose |
| :--- | :--- | :--- |
| **Swarms** | `ruflo` | Multi-agent swarm coordination for synthesis. |
| **Graphing** | `graphify` | Knowledge graph generation for routing maps. |

## Execution Rule
When a route activates one of these tools, the agent must verify the output against the tool's specific SOP (Standard Operating Procedure) to ensure "Surgical" precision.
