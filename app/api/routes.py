from fastapi import APIRouter, HTTPException

from app.agent.graph import agent
from app.api.schemas import QuestionRequest, QuestionResponse

router = APIRouter()


@router.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):

    print("\n========== NEW REQUEST ==========")
    print("Question:", request.question)

    try:
        result = agent.invoke({
            "question": request.question,
            "schema": "",
            "sql": "",
            "query_results": {},
            "answer": "",
            "error": ""
        })

        print("AGENT RESULT:", result)

        if result.get("error"):
            raise HTTPException(status_code=400, detail=result["error"])

        return QuestionResponse(
            question=request.question,
            sql=result["sql"],
            results=result["query_results"],
            answer=result["answer"]
        )

    except HTTPException:
        raise

    except Exception as e:
        import traceback

        print("\n========== FULL ERROR ==========")
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )