import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.weather_agent import get_weather

result = get_weather("Goa", 3)
print(result)