from mcp.server.fastmcp import FastMCP, Context
import time
import logging

mcp = FastMCP("add_integers")

# defining the MCPError class
class MCPError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}")


# defining how the logger should work
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='./mcp_server.log',
    filemode='a',
    force=True
)

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
    logging.info(f"Adding {a} and {b}")
    result = a + b
    logging.info(f"The result is {result}.")
    return result


# defining a divide tool to the MCP
@mcp.tool()
def divide(a: int, b: int) -> float:
    '''
    Divide an integer by another and return the quotient

    Args:
        a: The numerator
        b: The denominator

    Returns:
        The result of the division.
    '''
    if b == 0:
        return MCPError(code=400, message="Division by zero is not allowed!")

    return a / b

@mcp.tool()
def long_process(steps: int):
    """
    Simulates a long-running process.
    """
    for i in range(steps):
        print(f"Processing step {i + 1} of {steps}")
        time.sleep(0.1)
    return "Process complete!"


if __name__ == "__main__":
    mcp.run(transport='stdio')