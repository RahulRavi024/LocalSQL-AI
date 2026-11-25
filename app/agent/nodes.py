from app.database.executor import execute_sql
from app.database.schema import get_schema_for_llm
from app.services.analyzer import analyze_results
from app.sql.generator import generate_sql
from app.sql.validator import validate_sql


def schema_node(state):

    schema = get_schema_for_llm()

    return {
        "schema": schema
    }


def sql_generation_node(state):
    print("\n========== SQL GENERATION START ==========")

    sql = generate_sql(state["question"])

    print("\n========== GENERATED SQL ==========")
    print(sql)
    print("\n========== SQL GENERATION END ==========\n")

    # Prevent LLM error messages from being treated as SQL
    if not sql or sql.startswith("Error:"):
        return {
            "sql": "",
            "error": sql or "SQL generation failed"
        }

    return {
        "sql": sql
    }
    
def validation_node(state):

    is_valid, result = validate_sql(state["sql"])

    if not is_valid:

        return {
            "error": result
        }

    return {
        "sql": result,
        "error": ""
    }


def execution_node(state):

    results = execute_sql(state["sql"])

    return {
        "query_results": results
    }


def analysis_node(state):

    answer = analyze_results(
        question=state["question"],
        sql=state["sql"],
        results=state["query_results"]
    )

    return {
        "answer": answer
    }