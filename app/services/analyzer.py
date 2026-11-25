from app.llm.model import ask_llm


def analyze_results(question: str, sql: str, results: dict) -> str:

    prompt = f"""
You are a financial data analyst.

USER QUESTION:
{question}

SQL QUERY:
{sql}

QUERY RESULTS:
{results}

Instructions:
- Answer the user's original question using the results.
- Be concise and clear.
- Do not invent data.
- If there are no results, say no matching records were found.
- Mention important patterns when relevant.
- Use the actual numbers from the results.
"""

    answer = ask_llm(prompt)

    return answer