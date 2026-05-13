# 🧠 Surgical Brain OS: A Deterministic Framework for LLM Orchestration

## 🌌 The Vision: From Probabilistic Prompting to Deterministic Routing

Most modern AI agents operate on **Probabilistic Prompting**. They "search" for information, "guess" the best tool, and "hope" the LLM follows the instructions. This leads to **Cognitive Drift**, **Token Bloat**, and **Hallucinations**.

**Surgical Brain OS** replaces "guessing" with **Routing**. 

Instead of asking an LLM to "find the answer," this framework treats the AI's context window as **RAM** and the external knowledge base as a **Disk**. It uses a deterministic "Neural Map" to route the request through a precise chain of functional nodes, loading only the exact "pages" of memory required for the task.

---

## 🚀 The Core Innovation: The 4-Tier Escalation Ladder

To eliminate noise and maximize precision, every request is passed through the **Escalation Ladder**. The system only activates the minimum level of intelligence required:

### 🟢 L1: Surgical-Lite (Direct Execution)
For trivial requests (e.g., "What is the current date?"). Direct execution with zero overhead.

### 🟡 L2: Operational Index (Route Mapping)
When the request is known but requires specific context. The system queries the `graph.json` (The Surgical Web) to find the deterministic path to the answer.

### 🟠 L3: Functional Nodes (Targeted Execution)
Once the route is found, the system activates specific **Surgical Nodes**. These are high-precision wrappers around tools like **Polars** (for cleaning), **sqlglot** (for transpilation), and **langextract** (for grounded extraction).

### 🔴 L4: Orchestrated (Complex Synthesis)
For high-complexity tasks. The system executes a multi-node pipeline and performs a final **Sovereign Alignment** check to ensure the output adheres to strict technical and ethical constraints.

---

## 🕸️ The Surgical Web & Knowledge Graphing

Traditional RAG retrieves *documents*. The Surgical Web retrieves **Routes**.

The heart of the system is a Knowledge Graph (`graph.json`). This graph ensures that if a task requires "Cleaning $\to$ Verification $\to$ Synthesis," the AI **cannot** skip a step or launder the data through an incorrect tool. It transforms the LLM from a "creative writer" into a "precision operator."

## 🛡️ The Sovereign State: Zero-Drift Alignment

The final gate of every L4 process is the **Sovereign State**. This is a set of immutable constraints (Technical, Ethical, and Stylistic). 

No output is delivered to the user until the `SovereignValidator` confirms that the result:
1. Matches the required technical dialect (e.g., Snowflake SQL).
2. Adheres to the precision constraints (e.g., 2-decimal rounding).
3. Maintains the professional "voice" of the architect.

---

## 🛠️ Quick Start

### 1. Installation
```bash
git clone https://github.com/pramishmaharjan/Deterministic-Framework-for-LLM-Orchestration.git
cd surgical-brain-os
python scripts/setup_env.py
```

### 2. Configuration
The framework is designed for zero-config startup. On the first run, the system will:
1. Automatically create a local `config/` directory with sample routing and sovereign templates.
2. Initialize a "Brain Root" (external data store) in your home directory or `D:/` drive (Windows).

If you wish to use a custom location for your brain data, edit the generated `.env` file and define your `BRAIN_ROOT_PATH`.

### 3. Run Proof of Concept
```bash
python examples/basic_routing.py
```

## 📈 Expected Outcomes
- **Token Reduction:** Up to 70% reduction in context overhead.
- **Zero Hallucination:** Deterministic paths eliminate "creative" guesses.
- **Absolute Consistency:** Sovereign alignment ensures identical output quality regardless of LLM temperature.

---
*This repository provides the production-grade Architectural Skeleton. The high-precision routing weights and proprietary prompt kernels are omitted to preserve core intellectual property. For collaboration or full implementation, please contact the author.*
