# Sovereign State Specification

The Sovereign State is the final alignment layer of the Surgical Brain. It prevents "AI Drift" and ensures that the system's outputs remain consistent with the architect's intent.

## Core Functions
1. **Value Alignment**: Ensures the output matches the defined professional and ethical standards.
2. **Technical Constraints**: Enforces strict rules (e.g., "All SQL must be in Snowflake dialect," "All decimals must be rounded to 2 places").
3. **Contextual Anchor**: Acts as the "North Star" for the AI, reminding it of the ultimate goal of the project.

## Integration
Every L4 (Orchestrated) task must end with a "Sovereign Check" where the AI compares its proposed result against the `Sovereign_State.md` and adjusts the output before delivery.
