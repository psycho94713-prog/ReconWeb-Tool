from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/history",
    tags=["History"]
)

@router.get("/")
async def get_history():
    return {
        "message": "History module working",
        "data": []
    }