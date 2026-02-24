from .base import post, get
import json

def search_bus_api_call(payload):
    apiResponse = None

    if(payload['traveldate'] ==  None):
       del payload['traveldate']
    
    apiResponse = post("/user/search",payload)
       
    return json.dumps(apiResponse)

def search_bus_tool(from_city: str, to_city: str, date: str | None):

    payload = {
        "from": from_city,
        "to": to_city,
        "traveldate": date
    }

    return search_bus_api_call(payload)

