import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.recommendation_agent import generate_recommendations

result = generate_recommendations("Goa", ["beaches", "nightlife"], "mid")
print(result)