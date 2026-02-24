from typing import List
from pydantic import BaseModel, Field
from .base import post
import json


# ---------- Core function ----------
def get_all_seats(
    tripId: str,
    from_city: str,
    to_city: str,
    traveldate: str,
    token : str
):
    

    payload = {
        "tripId": tripId,
        "from": from_city,
        "to": to_city,
        "traveldate": traveldate,
    }


    headers = {
        "Authorization": f"Bearer {token}"
    }

    res = post("/ticket/seat/get", payload, headers=headers)


    if not res.get("success"):
        print("Seat fetch failed")

    
    return  json.dumps(res.get("bookedseat", []))


