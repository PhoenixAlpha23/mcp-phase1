from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SEOWriter")

@mcp.tool()
def seo_blog_draft(topic: str, tone: str) -> str:
    return f"Draft ({tone}) on {topic}: ..."

if __name__ == "__main__":
    mcp.run(transport="streamable_http", port=9000)
