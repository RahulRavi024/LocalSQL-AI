from sqlalchemy import text

from app.database.connection import engine
from app.sql.validator import validate_sql


def execute_sql(sql: str):

    is_valid, result = validate_sql(sql)

    if not is_valid:
        raise ValueError(result)

    with engine.connect() as connection:

        query_result = connection.execute(text(result))

        columns = list(query_result.keys())

        rows = query_result.fetchall()

        data = [
            dict(zip(columns, row))
            for row in rows
        ]

    return {
        "columns": columns,
        "rows": data,
        "row_count": len(data)
    }