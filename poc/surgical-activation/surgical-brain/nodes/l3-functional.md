# SOP: L3 - Functional Execution

## Purpose
Execute specific tools or logic nodes with high precision and verified state.

## Execution Protocol
1. **Node Load**: Read the specific implementation detail of the functional node.
2. **Surgical Action**:
   - **Verify**: Check current state.
   - **Execute**: Run the command/tool.
   - **Validate**: Verify the output against the expected result.
3. **State Update**: Store the result in local memory for the next node in the sequence.

## Failure Condition
If the tool returns an unexpected error or the result fails validation $\to$ **Stop and report the specific failure point**.
