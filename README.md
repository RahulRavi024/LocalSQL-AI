# LocalSQL-AI

🗄️ A local natural language interface for querying MySQL databases using an LLM.

LocalSQL-AI allows users to interact with a MySQL database using plain English instead of manually writing SQL queries. It uses a locally running LLM through Ollama to generate SQL, validates the generated query, executes it against the database, and provides a natural language explanation of the results.

<img width="1882" height="991" alt="image" src="https://github.com/user-attachments/assets/7aa2f14e-9af6-4a7c-abe1-c1df50428f15" />

## ✨ Features

- 💬 Natural language to SQL query generation
- 🧠 Local LLM inference using Ollama
- 🔗 MySQL database integration
- 📋 Automatic database schema retrieval
- 🛡️ SQL query validation
- ⚡ Query execution using SQLAlchemy
- 📊 Natural language analysis of query results
- 🔄 LangGraph-based workflow orchestration
- 🖥️ Streamlit user interface
- 🚀 FastAPI backend

## 🏗️ Architecture

```text
User Question
     |
     v
Streamlit Frontend
     |
     v
FastAPI Backend
     |
     v
LangGraph Workflow
     |
     +--> Retrieve Database Schema
     |
     +--> Generate SQL using Ollama
     |
     +--> Validate SQL
     |
     +--> Execute Query against MySQL
     |
     +--> Analyze Results
     |
     v
Response to User
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| FastAPI | Backend API |
| Streamlit | Frontend interface |
| LangGraph | Workflow orchestration |
| Ollama | Local LLM inference |
| Qwen2.5-Coder 7B | SQL generation |
| MySQL | Database |
| SQLAlchemy | Database connectivity and execution |
| Requests | HTTP communication with Ollama |
| Pydantic | Data validation |

## 📁 Project Structure

```text
LocalSQL-AI/
│
├── app/
│   ├── agent/
│   │   ├── graph.py
│   │   ├── nodes.py
│   │   └── state.py
│   │
│   ├── api/
│   │   ├── routes.py
│   │   └── schemas.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── executor.py
│   │   └── schema.py
│   │
│   ├── llm/
│   │   └── model.py
│   │
│   ├── services/
│   │   └── analyzer.py
│   │
│   ├── sql/
│   │   ├── generator.py
│   │   ├── prompt.py
│   │   └── validator.py
│   │
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── tests/
│
├── .env.example
├── .gitignore
└── requirements.txt
```

## ⚙️ How It Works

1. The user enters a question through the Streamlit interface.
2. Streamlit sends the request to the FastAPI backend.
3. LangGraph manages the workflow.
4. The database schema is retrieved to provide context to the LLM.
5. Ollama generates an SQL query using the schema and user question.
6. The generated SQL is extracted and validated.
7. The query is executed against the MySQL database.
8. The returned data is passed to the analysis component.
9. The application presents the query results and a natural language explanation.

## 💡 Example Queries

Instead of writing SQL manually, users can ask:

```text
Show me the first 3 expenses.

What is the total spending for each category?

Show me all transactions from the last 7 days.

What is the average amount of my expenses?

What are my highest and lowest expenses?

Show expenses greater than 100 in the last 30 days.
```

The application generates the corresponding SQL queries, executes them, and returns the results.

## 📦 Requirements

- Python 3.10+
- MySQL Server
- Ollama
- Git

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/LocalSQL-AI.git
cd LocalSQL-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up Ollama

Download Ollama:

https://ollama.com/download

Pull the required model:

```bash
ollama pull qwen2.5-coder:7b
```

Make sure Ollama is running before starting the application.

### 5. Configure MySQL

Create your MySQL database and configure your connection.

Create a `.env` file in the project root:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/database_name
```

Replace the placeholders with your actual database credentials.

### 6. Start the FastAPI backend

```bash
uvicorn app.main:app --reload
```

Backend:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

### 7. Start the Streamlit frontend

Open a separate terminal and run:

```bash
streamlit run frontend/app.py
```

Frontend:

http://localhost:8501

## 🔒 Security

- Database credentials are stored in environment variables.
- `.env` is excluded from version control.
- SQL queries are validated before execution.

## 🔮 Future Improvements

- Improved SQL validation and error handling
- Support for additional database systems
- Better handling of complex queries
- Conversation history and follow-up questions
- Query optimization and improved schema context
- Enhanced database access controls

## 📌 Limitations

- SQL generation depends on the selected LLM.
- Query accuracy depends on schema context and the clarity of the question.
- Local inference performance depends on available hardware.
- Currently designed for MySQL databases.

---

Developed as a project to explore local LLM integration, natural language to SQL generation, and AI-driven database interaction.
