from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from io import BytesIO

from app.modules.report_generator import generate_report

router = APIRouter(
    prefix="/api/v1/report",
    tags=["Report"]
)


@router.post("/pdf")
async def generate_pdf(data: dict):

    pdf = generate_report(data)

    return StreamingResponse(
        BytesIO(pdf),
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            "attachment; filename=osint_report.pdf"
        }
    )