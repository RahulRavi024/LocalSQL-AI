from app.llm.model import ask_llm

question = "What is the capital of France? Answer in one sentence."

answer = ask_llm(question)

print("\nAI Response:")
print(answer)