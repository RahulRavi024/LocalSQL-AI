import sqlparse
from sqlparse.tokens import Keyword

ALLOWED_COMMANDS = {"SELECT"}

FORBIDDEN_KEYWORDS = {
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "REPLACE",
    "GRANT",
    "REVOKE",
    "EXECUTE",
}


def clean_sql(sql: str) -> str:

    sql = sql.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    if sql.startswith("<think>"):
        sql = sql.split("</think>")[-1].strip()

    return sql.strip()


def validate_sql(sql: str) -> tuple[bool, str]:

    sql = clean_sql(sql)

    parsed = sqlparse.parse(sql)

    if not parsed:
        return False, "Empty SQL query"

    if len(parsed) != 1:
        return False, "Multiple SQL statements are not allowed"

    statement = parsed[0]

    command = statement.get_type()

    if command not in ALLOWED_COMMANDS:
        return False, "Only SELECT queries are allowed"

    tokens = [
        token.value.upper()
        for token in statement.flatten()
        if token.ttype in Keyword
    ]

    for keyword in tokens:
        if keyword in FORBIDDEN_KEYWORDS:
            return False, f"Forbidden SQL keyword: {keyword}"

    return True, sql