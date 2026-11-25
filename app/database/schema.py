from sqlalchemy import inspect

from app.database.connection import engine


def get_database_schema():

    inspector = inspect(engine)

    schema_info = {}

    tables = inspector.get_table_names()

    for table in tables:

        columns = inspector.get_columns(table)

        column_info = []

        for column in columns:
            column_info.append({
                "name": column["name"],
                "type": str(column["type"]),
                "nullable": column["nullable"]
            })

        schema_info[table] = column_info

    return schema_info

def get_schema_for_llm():

    schema = get_database_schema()

    formatted_schema = "DATABASE SCHEMA:\n\n"

    for table, columns in schema.items():

        formatted_schema += f"Table: {table}\n"

        for column in columns:
            formatted_schema += (
                f"- {column['name']}: {column['type']}\n"
            )

        formatted_schema += "\n"

    return formatted_schema