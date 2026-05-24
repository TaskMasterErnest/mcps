from mcp.server.fastmcp import FastMCP

mcp = FastMCP("add_integers")

# creating a tool (from a method)
@mcp.tool() # a decorator to tell the MCP to expose this to others can use.
def add(a: int, b: int) -> int:
    '''
    Add two integers and return the sum

    Args:
        a: First integer
        b: Second integer

    Returns:
        The sum of a and b.
    '''

    return a + b


if __name__ == "__main__":
    mcp.run(transport='stdio')