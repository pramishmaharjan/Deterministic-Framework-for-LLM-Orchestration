# SOP: L1 - Surgical Direct

## Purpose
Handle trivial requests that require no external routing or complex synthesis.

## Execution Protocol
1. **Context Check**: Is the answer present in the current conversation context?
2. **Command Check**: Can the request be solved with a single, non-destructive tool call?
3. **Deliver**: Provide the result in a "Surgical" format.

## Failure Condition
If the request requires reading a file not yet in context, or involves multi-step logic $\to$ **Escalate to L2**.
