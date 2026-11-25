from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="LocalSQL-AI",
    description="Local LLM-powered MySQL assistant",
    version="1.0.0"
)


app.include_router(router, prefix="/api")