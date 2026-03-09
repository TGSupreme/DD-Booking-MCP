from fastmcp import FastMCP
from tools.search_bus import search_bus_tool
from tools.login import validate_tool
from tools.seats import get_all_seats
from tools.create_ticket import create_ticket_tool 
from tools.get_tickets import get_tickets_tools, get_ticket_details_tool
from tools.cancel_ticket import cancle_ticket_tool
import json

from pydantic import BaseModel, Field

class Passenger(BaseModel):
    name: str = Field(..., description="Passenger full name")
    age: int = Field(..., description="Passenger age")
    gender: str = Field(..., description="Passenger gender: male/female/other")

mcp = FastMCP(name = "QuickBus-MCP-Server")



@mcp.tool()
def search_bus(from_city: str, to_city: str, date: str | None):
    """This tool return the list of buses between two cities"""

    return search_bus_tool(from_city, to_city, date)

@mcp.tool()
def auth(email:str):
    """ this tool generate the otp for the user validation on the QuickBus server."""
    response = {
        "message" : "OTP generated successfully."
    }
    
    return json.dumps(response)

@mcp.tool()
def validate(email: str, otp: str): 
    """this tool validates the user using email and OTP and return token that is required for some tasks"""
    return validate_tool(email, otp)

@mcp.tool()
def get_available_seats(tripId: str,
    from_city: str,
    to_city: str,
    traveldate: str,
    
    token : str
    ):
    """ this tool   Fetch already booked seats for a selected trip.
        An empty list means all seats are available."""
    
    return get_all_seats(tripId,from_city, to_city,traveldate,token)

@mcp.tool()
def create_ticket(
    tripId: str,
    from_city: str,
    to_city: str,
    price: float,
    seats: list[int],
    passengers: list[Passenger],
    ticketdate: str,
    token: str,
):
    """This tool is used to book a ticket and return the details of ticket number of seats must be equal to number of passengers"""

    return create_ticket_tool(tripId, from_city, to_city, price, seats, passengers, ticketdate, token)


@mcp.tool()
def get_tickets(token: str):
    """this tool returns all the tickets of a user """
    return get_tickets_tools(token)

@mcp.tool()
def get_ticket_details(ticketId:str , token: str):
    """this Tool returns the details of specific ticket by ticketID """
     
    return get_ticket_details_tool(ticketId , token)

@mcp.tool()
def cancle_ticket(ticketId : str, token:str):
    """This tool is used to cancle ticket using ticketId"""

    return cancle_ticket_tool(ticketId, token)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
