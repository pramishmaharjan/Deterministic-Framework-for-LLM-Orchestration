# Sovereign State Specification

The **Sovereign State** is the final alignment layer of the Surgical Brain. It is the "North Star" that prevents AI drift.

## The Philosophy of Alignment
An LLM can be technically correct but "architecturally wrong." The Sovereign State ensures that the output is not only accurate but also adheres to the specific constraints of the system's owner.

## Core Functions
1. **Technical Constraints:** 
   - Enforces specific SQL dialects (e.g., Snowflake, BigQuery).
   - Mandatory rounding rules (e.g., 2 decimal places).
   - Strict naming conventions for data frames.
2. **Value Alignment:** 
   - Ensures the tone is "Surgical" (concise, direct, evidence-based).
   - Prohibits "conversational filler" (e.g., "Here is the result you asked for...").
3. **Verification Gate:** 
   - The Sovereign State acts as a boolean gate. If the output does not pass the alignment check, it is sent back to the L4 Orchestrator for correction.

## Implementation in Code
The `SovereignValidator` class reads the `sovereign_state.md` file and compares the final output against these rules using a high-precision validation prompt.
