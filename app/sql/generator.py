import re

from app.database.schema import get_schema_for_llm
from app.llm.model import ask_llm
from app.sql.prompt import build_sql_prompt


def extract_sql(response: str) -> str:

    # First, try to extract SQL from a markdown code block
    code_block = re.search(
        r"```(?:sql)?\s*(.*?)```",
        response,
        re.IGNORECASE | re.DOTALL
    )

    if code_block:
        response = code_block.group(1)

    # Find the actual SELECT query
    sql_match = re.search(
        r"\bSELECT\b.*?;",
        response,
        re.IGNORECASE | re.DOTALL
    )

    if not sql_match:
        raise ValueError("No valid SELECT query found in LLM response.")

    sql = sql_match.group(0).strip()

    return sql


def generate_sql(question: str) -> str:

    schema = get_schema_for_llm()

    prompt = build_sql_prompt(
        question=question,
        schema=schema
    )

    raw_response = ask_llm(prompt)

    print("\n========== RAW OLLAMA RESPONSE ==========")
    print(raw_response)
    print("=====================================")

    sql_query = extract_sql(raw_response)

    print("\n========== CLEANED SQL ==========")
    print(sql_query)
    print("===============================\n")

    return sql_query