from fastmcp import FastMCP
from tools.search_bus import search_bus_tool
from tools.login import login_tool
from tools.seats import get_all_seats
from pydantic import BaseModel, Field
from tools.create_ticket import create_ticket_tool 

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
def login(email: str, password: str):
    """this tool log in the user into the system and return token that is required for some tasks"""
    return login_tool(email, password)

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

if __name__ == "__main__":
    mcp.run()
