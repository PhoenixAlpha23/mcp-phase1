from mcp.server.fastmcp import FastMCP

mcp= FastMCP("weather")

@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Get the current weather for a specified city.
    
    :param city: The name of the city to get the weather for.
    :return: A string describing the current weather in the city.
    """
    # Simulated response for demonstration purposes
    return f"The current weather in {city} is sunny with a temperature of 25°C."

if __name__ == "__main__":
    mcp.run()