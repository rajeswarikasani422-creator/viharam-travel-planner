import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.itinerary_agent import generate_itinerary

result = generate_itinerary("Goa", 3, ["beaches", "nightlife"])
print(result)