from pydantic import BaseModel
import uuid

class Request_entry(BaseModel):
    vehicleNumber : str
    vehicleType : str

class Response_entry(BaseModel):
    ticketId : str | None = None
    slot : str | None = None
    vehicleType : str | None = None
    status : str = "PARKED"



class Request_exit(BaseModel):
    ticketId: str
    minutesParked : int

class Response_exit(BaseModel):
    ticketId : str | None = None
    slot : str | None = None
    fee : int | None = None
    status : str = "EXITED"


