# 🧠 Surgical Brain OS
A deterministic framework for LLM orchestration, shifting AI from "probabilistic prompting" to "deterministic routing."

## 🚀 Quick Start

### 1. Setup
```bash
git clone https://github.com/pramishmaharjan/Deterministic-Framework-for-LLM-Orchestration.git
cd surgical-brain-os
pip install -r requirements.txt
cp .env.example .env
```

### 2. Run the Proof of Concept
Run the basic routing example to see the **4-Tier Escalation Ladder** in action:
```bash
python examples/basic_routing.py
```

## 🏗️ Architecture: The Escalation Ladder

The Surgical Brain prevents token bloat and cognitive drift by loading only the necessary "pages" of memory required for a task:

- **L1 (Surgical-Lite)**: Direct execution for trivial requests.
- **L2 (Operational Index)**: Mapping the request via `graph.json` to find the route.
- **L3 (Functional Nodes)**: Executing specific surgical tools (e.g., Polars, sqlglot).
- **L4 (Orchestrated)**: Complex tool-chaining with final **Sovereign State** alignment.

## 🕸️ The Surgical Web
Instead of "searching," the system "routes." 
Example: `Raw Text` $\to$ `Extraction` $\to$ `Cleaning` $\to$ `Verification` $\to$ `Sovereign Alignment`.

## 🛡️ The Sovereign State
Every high-complexity output is validated against the `sovereign_state.md` to ensure technical constraints and value alignment are met before delivery.

## 🛠️ Implementation Note
This repository provides the **Architectural Skeleton**. The high-precision routing weights and proprietary "Surgical" prompt kernels are omitted to preserve core intellectual property. 

For collaboration or full implementation details, please contact the author.
