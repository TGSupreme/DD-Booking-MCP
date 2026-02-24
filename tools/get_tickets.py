from .base import get
import json

def get_tickets_tools(token):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    res = get("/ticket/user/get", headers)

    return json.dumps(res.get("allticket"))


def get_ticket_details_tool(ticketId, token):
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    res = get(f"/ticket/user/{ticketId}", headers)

    return json.dumps(res.get("ticket"))
