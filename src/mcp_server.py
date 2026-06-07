from mcp.server.fastmcp import FastMCP
from .router import triage
from .executor import executor

# Initialize FastMCP server
mcp = FastMCP("BrainOS-Manager")

@mcp.tool()
async def brain_route(request: str) -> str:
    """
    Determines the complexity tier (L1-L4) and required effort for a request.
    Use this FIRST before calling brain_execute.
    """
    route = triage.route(request)
    return str(route)

@mcp.tool()
async def brain_execute(tier: str, request: str, context: str = "{}") -> str:
    """
    Executes the request using the appropriate L-tier tool stack and reasoning depth.
    L1: Operational, L2: Functional, L3: Analytical, L4: Orchestrated.
    """
    import ast
    ctx = ast.literal_eval(context) if context else {}
    result = await executor.execute(tier, request, ctx)
    return result

if __name__ == "__main__":
    mcp.run()
