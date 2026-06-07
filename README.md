# Deterministic Framework for LLM Orchestration (BrainOS v2.0)

## 🧠 The Vision: From Probabilistic to Deterministic
Most LLM interactions are probabilistic—the model "guesses" the best path. **BrainOS** transforms this into a deterministic cognitive operating system. It treats the LLM as a high-level manager that routes requests through a surgically precise pipeline, ensuring that reasoning depth is always matched to task complexity.

## 🏗️ The Architecture: The 4-Tier Escalation Ladder
BrainOS doesn't use a "one size fits all" prompt. Every request is routed via the **Surgical Router** into one of four complexity tiers:

### L1: Surgical-Operational (Standard Effort)
**Goal:** Instant, high-precision retrieval.
**Path:** `User Request` $\rightarrow$ `Graphify` $\rightarrow$ `Surgical Read` $\rightarrow$ `Result`.
**Use Case:** "What is the budget for Project X?"

### L2: Functional Logic (Standard/High Effort)
**Goal:** Understanding dependencies and cross-component relationships.
**Path:** `User Request` $\rightarrow$ `Graphify BFS` $\rightarrow$ `Surgical Read` $\rightarrow$ `Sovereign State` $\rightarrow$ `Result`.
**Use Case:** "How does the authentication flow affect the database schema?"

### L3: Analytical Crunch (xhigh Effort)
**Goal:** High-volume data transformation and structural analysis.
**Path:** `User Request` $\rightarrow$ `LangStruct` $\rightarrow$ `Polars` $\rightarrow$ `DuckDB` $\rightarrow$ `dbt` $\rightarrow$ `Surgical Semantic Layer` $\rightarrow$ `Result`.
**Use Case:** "Analyze the top 5 outliers in the performance dataset."

### L4: Orchestrated Synthesis (Max Effort)
**Goal:** Complex software engineering, architecture, and multi-step research.
**Path:** `User Request` $\rightarrow$ `DeepAgent Manager` $\rightarrow$ `ruflo Swarm` $\rightarrow$ `LangGraph Cycle` (Reason $\rightarrow$ Rubric $\rightarrow$ Correct) $\rightarrow$ `Sovereign State` $\rightarrow$ `Surgical Semantic Layer` $\rightarrow$ `Result`.
**Use Case:** "Refactor the entire API layer to support multi-tenancy."

---

## 🛠️ The Intelligence Stack

### 1. The Orchestration Layer (The Brain)
*   **DeepAgents:** The central manager using **LangGraph** to maintain state and execute cyclic, self-correcting workflows.
*   **ruflo:** An MCP-based swarm engine used to spawn and coordinate specialized agents for L4 tasks.
*   **Surgical Router:** A deterministic triage engine that assigns the correct Effort Level to avoid token waste.

### 2. The Analytical Layer (The Muscle)
*   **LangStruct & LangExtract:** High-precision, schema-based extraction with absolute source grounding.
*   **Polars & DuckDB:** The high-performance data stack for transforming and querying structural knowledge.
*   **dbt:** Ensuring data quality through tested SQL transformation pipelines.

### 3. The Guardrail Layer (The Truth)
*   **Sovereign State:** The root of trust. Every result is validated against project invariants to ensure zero-drift alignment.
*   **Surgical Semantic Layer:** Translates technical extraction entities into business-facing definitions.

---

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/pramishmaharjan/Deterministic-Framework-for-LLM-Orchestration.git
cd Deterministic-Framework-for-LLM-Orchestration

# Setup the BrainOS Service
pip install -r requirements.txt
python scripts/setup_brain_os.py
```

### Usage
The system is designed to be used as an MCP server. Once running, you can interact with the Brain via:
*   `brain_route(request)`: To classify the complexity.
*   `brain_execute(tier, request)`: To trigger the surgical pipeline.

## 📊 Token ROI
By shifting to a **Logarithmic Scaling** model, BrainOS achieves:
*   **~90% Reduction** in input tokens via Surgical Reads.
*   **Constant-time Context** via LangGraph DeltaChannels.
*   **Reasoning Efficiency** by matching Effort Level $\rightarrow$ Complexity Tier.

---
*Deterministic. Surgical. Sovereign.*
