from typing import TypedDict


class AgentState(TypedDict):

    question: str

    schema: str

    sql: str

    query_results: dict

    answer: str

    error: str