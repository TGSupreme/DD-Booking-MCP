from .base import put

def cancle_ticket_tool(ticketId: str, token:str):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    res = put(f"/ticket/{ticketId}", headers)

    return res