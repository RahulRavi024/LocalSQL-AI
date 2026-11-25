from app.database.schema import get_database_schema

schema = get_database_schema()

for table, columns in schema.items():

    print(f"\nTable: {table}")

    for column in columns:
        print(
            f"  {column['name']} | "
            f"{column['type']} | "
            f"Nullable: {column['nullable']}"
        )