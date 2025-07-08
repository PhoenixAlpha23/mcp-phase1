from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

async def init_agent():
    client = MultiServerMCPClient({
        "seo": {"url": "http://localhost:9000/mcp", "transport": "streamable_http"},
    })
    tools = await client.get_tools()
    agent = create_react_agent("openai:gpt-4o", tools)
    return agent
