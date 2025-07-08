from fastapi import FastAPI, Request
from agent import init_agent

app = FastAPI()
agent = None

@app.on_event("startup")
async def startup():
    global agent
    agent = await init_agent()

@app.post("/run")
async def run_endpoint(req: Request):
    body = await req.json()
    res = await agent.ainvoke({"messages": [{"role": "user", "content": body["prompt"]}]})
    return {"response": res}
