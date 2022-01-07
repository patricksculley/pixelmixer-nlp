from fastapi import APIRouter
from app.models.NERInput import NERInput
from app.services.nerService import NerService

router = APIRouter(prefix='/ner', tags=['ner'], responses={404: {"description": "Not found"}})
ner_service = NerService()

@router.post("/recognizeBasicText")
async def get_ner(input: NERInput):
    result = ner_service.process_text(input.text)
    return result
