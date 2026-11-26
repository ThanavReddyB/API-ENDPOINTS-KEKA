import logging
from fastapi import APIRouter
from app.models import SampleRequest, SampleResponse
from app import storage

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/sample", response_model=SampleResponse)
def create_sample(body: SampleRequest):
    logger.info("POST /sample  name=%s value=%s", body.name, body.value)
    result = storage.save(body.name, body.value)
    logger.info("Created item id=%s", result.id)
    return result
