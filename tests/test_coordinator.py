import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.coordinator_agent import run_coordinator

trip = {
    "total_budget": 50000,
    "num_days": 5,
    "num_people": 2,
    "destination_tier": "mid"
}

result = run_coordinator(trip)
print(result)