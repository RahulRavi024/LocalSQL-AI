from app.agent.nodes import (
    analysis_node,
    execution_node,
    schema_node,
    sql_generation_node,
    validation_node,
)
from langgraph.graph import END, START, StateGraph

from app.agent.state import AgentState


def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node("schema", schema_node)
    graph.add_node("generate_sql", sql_generation_node)
    graph.add_node("validate_sql", validation_node)
    graph.add_node("execute_sql", execution_node)
    graph.add_node("analyze", analysis_node)

    graph.add_edge(START, "schema")

    graph.add_edge("schema", "generate_sql")

    graph.add_edge("generate_sql", "validate_sql")

    graph.add_edge("validate_sql", "execute_sql")

    graph.add_edge("execute_sql", "analyze")

    graph.add_edge("analyze", END)

    return graph.compile()


agent = build_graph()