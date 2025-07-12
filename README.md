# 🧠 Agents and tool creation using LangGraph & MCP

## 🛠️ Tech Stack

- **LangGraph** – for defining multi-step agent workflows with tool-aware nodes  
- **Model Context Protocol (MCP)** – modular protocol to serve tools over HTTP  
- **FastAPI** – lightweight backend for hosting the agent API  
- **uv + pyproject.toml** – modern Python project management  
- **curl (or custom frontend)** – for testing and triggering the agent  
- Optional: OpenAI GPT, LanguageTool, Sapling, or Grammarly APIs  

---

## 🎯 Objective

This project aims to build an intelligent **AI Copywriter agent** capable of generating, analyzing, and refining written content tailored to brand-specific guidelines. The system is designed to act as a multi-skilled assistant that:

- Draft SEO-optimized blog content  
- Generate tone-adaptive social media posts  
- Performs grammar, sentiment, and coherence refinements  
- Detect potential plagiarism or style violations  

The solution is highly modular, allowing external tools to be integrated via MCP with minimal coupling, supporting robust experimentation and extension.

---

## 📂 Project Structure

mcp-copywriter/
├── mcp_servers/
│   └── seo_server.py          # A tool exposed via MCP (e.g., SEO content generation)
│   └── grammar_server.py      # (Optional) Grammar or sentiment tool as separate server
│
├── app/
│   ├── agent.py               # LangGraph-based agent using MCP clients + GPT
│   └── api.py                 # FastAPI app with `/run` endpoint
│
├── pyproject.toml             # Project metadata + dependencies (uv-based)
├── uv.lock                    # Lockfile for reproducible builds
├── .env                       # API keys and config (e.g., OpenAI keys)


---

## 🤖 Agent Flow

The agent is built with LangGraph’s `StateGraph`, consisting of one or more **ToolNode(s)** dynamically fetched from MCP-compatible servers. A sample workflow may look like:

1. **Input Prompt** from user  
2. → **SEO Draft Tool** (via `seo_server.py`)  
3. → **Grammar Refinement Tool** (optional)  
4. → Return response  

This design allows tools to evolve independently and be replaced or scaled as needed.

---

## 🔌 Tool Communication (MCP)

Each tool (e.g., blog draft, grammar checker) is hosted independently using the **MCP server interface**. These tools register functions (annotated with `@mcp.tool`) that the main agent can discover and invoke at runtime over HTTP.

---

## 🚀 Usage Flow

- Start the MCP tool servers (e.g., SEO tool at port 9000)  
- Run the FastAPI app which initializes a LangGraph agent with MCP-discovered tools  
- Send a POST request to `/run` with your writing prompt  
- The agent uses the appropriate tools and returns the refined content  

### Example `curl` command:

```bash
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Write a blog intro on sustainable packaging in retail."}'