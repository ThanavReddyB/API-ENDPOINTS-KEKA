import logging
from fastapi import APIRouter , HTTPException
from app.models import Response_entry , Request_entry , Request_exit , Response_exit
from app import storage

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post('/entry',response_model = Response_entry)
def parking(body : Request_entry):
    logger.info("request reached")
    result = storage.park(body.vehicleNumber , body.vehicleType)
    logger.info("result = %s", result)
    return result

@router.post('/exit',response_model = Response_exit)
def exitting(body : Request_exit):
    logger.info("request reached")
    result = storage.exit(body.ticketId , body.minutesParked)
    logger.info("result = %s", result)
    return result
