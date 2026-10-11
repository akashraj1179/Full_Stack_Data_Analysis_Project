from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
import subprocess

class AgentState(dict): pass

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def agent_node(state: AgentState):
    query = state["input"]

    if "compliance" in query.lower():
        # Run your compliance_engine.py pipeline
        result = subprocess.run(
            ["python", "compliance_engine.py"],
            capture_output=True, text=True
        )
        state["output"] = result.stdout
    else:
        # Default LLM reasoning
        response = llm.invoke(query)
        state["output"] = response.content

    return state

graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.set_entry_point("agent")
graph.add_edge("agent", END)

app = graph.compile()
