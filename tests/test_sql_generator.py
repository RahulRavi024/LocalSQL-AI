from app.sql.generator import generate_sql

question = "Show me my top 5 most expensive transactions"

sql = generate_sql(question)

print("\nGenerated SQL:")
print(sql)