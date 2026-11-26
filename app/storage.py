from app.models import Request_entry , Request_exit , Response_exit , Response_entry
import uuid
import logging
logger = logging.getLogger(__name__)

vehicles = {"BIKE" : ["B1","B2"], "CAR" : ["C1","C2"]}
_store1: dict[str , Request_entry] = {}
_store2: dict[str , Request_exit] = {}

def park(vehicleNumber : str , vehicleType : str) -> Response_entry | None:
    logger.info(vehicleType)
    ticketid = str(uuid.uuid4())
    result = Response_entry(ticketId = "1" , slot = "C1" , vechicleType = "LL",status = "PARKED" )
    # _store1[ticketid] = result
    return result


def exit(ticketid : str , minutesparked : int) -> Response_exit:
    if minutesparked // 60 == 0:
        hours = 1
    else:
        hours = minutesparked // 60
    fee = hours * 40
    result = Response_exit(ticketid = "2" , slot = "C1" , fee = fee , status = "EXITED")
    # _store2[ticketid] = result
    return result

