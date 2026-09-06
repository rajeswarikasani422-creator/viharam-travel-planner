from agents.budget_agent import calculate_budget
from agents.itinerary_agent import generate_itinerary
from agents.weather_agent import get_weather
from agents.recommendation_agent import generate_recommendations

def run_coordinator(trip_request):
    agent_responses = {}

    budget_result = calculate_budget(
        total_budget=trip_request["total_budget"],
        num_days=trip_request["num_days"],
        num_people=trip_request["num_people"],
        destination_tier=trip_request.get("destination_tier", "mid")
    )
    agent_responses["budget"] = budget_result

    itinerary_result = generate_itinerary(
        destination=trip_request["destination"],
        num_days=trip_request["num_days"],
        interests=trip_request.get("interests", [])
    )
    agent_responses["itinerary"] = itinerary_result

    weather_result = get_weather(
        destination=trip_request["destination"],
        num_days=trip_request["num_days"]
    )
    agent_responses["weather"] = weather_result

    recommendation_result = generate_recommendations(
        destination=trip_request["destination"],
        interests=trip_request.get("interests", []),
        destination_tier=trip_request.get("destination_tier", "mid")
    )
    agent_responses["recommendations"] = recommendation_result

    return {
        "trip_request": trip_request,
        "agent_responses": agent_responses,
        "status": "success"
    }