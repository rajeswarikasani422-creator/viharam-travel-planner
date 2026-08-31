from agents.budget_agent import calculate_budget

def run_coordinator(trip_request):
    agent_responses = {}

    budget_result = calculate_budget(
        total_budget=trip_request["total_budget"],
        num_days=trip_request["num_days"],
        num_people=trip_request["num_people"],
        destination_tier=trip_request.get("destination_tier", "mid")
    )
    agent_responses["budget"] = budget_result

    return {
        "trip_request": trip_request,
        "agent_responses": agent_responses,
        "status": "success"
    }