from typing import List
from pydantic import BaseModel, Field
from .base import post, put
import json

# ---------- Passenger schema ----------
class Passenger(BaseModel):
    name: str = Field(..., description="Passenger full name")
    age: int = Field(..., description="Passenger age")
    gender: str = Field(..., description="Passenger gender: male/female/other")


# ---------- Input schema ----------
class CreateTicketInput(BaseModel):
    tripId: str = Field(..., description="Trip ID of selected bus")
    from_city: str = Field(..., description="Source city name")
    to_city: str = Field(..., description="Destination city name")
    price: float = Field(..., description="Total ticket price")
    seats: List[int] = Field(..., description="List of seat numbers selected")
    passengers: List[Passenger] = Field(..., description="Passenger details. Count MUST equal number of seats exactly.")
    ticketdate: str = Field(..., description="Travel date in YYYY-MM-DD format")


# ---------- Core function ----------
def create_ticket_tool(
    tripId: str,
    from_city: str,
    to_city: str,
    price: float,
    seats: List[int],
    passengers: List[Passenger],
    ticketdate: str,
    token: str,
):

    if len(seats) != len(passengers):
        return ("PASSENGER_COUNT_MISMATCH")

    payload = {
        "tripId": tripId,
        "from": from_city,
        "to": to_city,
        "price": price,
        "seats": seats,
        "passengers": [p.dict() for p in passengers],
        "ticketdate": ticketdate,
    }
    print(f"payload by llm : {payload}")


    headers = {
        "Authorization": f"Bearer {token}"
    }

    res = post("/ticket/", payload, headers=headers)

    
    ticketId = (res.get("ticket")).get("_id")

    paymentPayload = {
        "price": price        
    }
    paymentRes = put(f"/ticket/update/payment/{ticketId}", paymentPayload, headers=headers)


    return json.dumps(paymentRes.get("updatedTicket"))
    