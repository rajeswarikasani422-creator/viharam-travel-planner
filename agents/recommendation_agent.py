import os
import google.generativeai as genai
from dotenv import load_dotenv
from agents.utils import parse_llm_json

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_recommendations(destination, interests, destination_tier="mid"):
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    Suggest local recommendations for a trip to {destination}.
    Traveler interests: {', '.join(interests)}.
    Budget tier: {destination_tier}.

    Return ONLY valid JSON in this exact format, no extra text:
    {{
      "recommendations": {{
        "food": ["food suggestion 1", "food suggestion 2"],
        "experiences": ["experience 1", "experience 2"],
        "packing_tips": ["tip 1", "tip 2"]
      }}
    }}
    """

    response = model.generate_content(prompt)
    parsed, error = parse_llm_json(response.text)

    if error:
        return {
            "recommendations": None,
            "raw_text": response.text,
            "source": "llm",
            "error": error
        }

    return {
        "recommendations": parsed["recommendations"],
        "source": "llm"
    }