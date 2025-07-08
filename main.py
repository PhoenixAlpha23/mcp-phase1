from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda

# Step 1: Define your state schema (can be a dict)
def starter_node(state):
    print("Hello from LangGraph!")
    return state

# Step 2: Build your graph
builder = StateGraph(dict)
builder.add_node("start", RunnableLambda(starter_node))
builder.set_entry_point("start")

# Step 3: Compile and run
graph = builder.compile()
graph.invoke({})