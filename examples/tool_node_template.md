# Tool Node Template (Surgical Blueprint)

Every tool in the Surgical Brain must have a corresponding Node file. This prevents the AI from "guessing" how a tool works.

## Template Structure
---
name: [tool-name]
description: [One-line purpose]
type: [tool/orchestrator/memory]
stage: [L1-L4]
---

### SOP (Standard Operating Procedure)
1. **Trigger**: When should this tool be used?
2. **Input**: What specific format does the tool require?
3. **Execution**: What are the critical flags or parameters?
4. **Output**: What does a "perfect" result look like?
5. **Surgical Constraint**: What is the one thing the AI must NOT do when using this tool?
