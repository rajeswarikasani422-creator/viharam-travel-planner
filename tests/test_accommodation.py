import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.accommodation_agent import suggest_accommodation

result = suggest_accommodation("Goa", 3, "mid", ["beaches", "nightlife"])
print(result)