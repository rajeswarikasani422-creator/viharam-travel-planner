import os
import google.generativeai as genai
from dotenv import load_dotenv
from agents.utils import parse_llm_json

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def suggest_accommodation(destination, num_days, destination_tier, interests):
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    Suggest accommodation for a {num_days}-day trip to {destination}.
    Budget tier: {destination_tier}.
    Traveler interests: {', '.join(interests)}.

    Return ONLY valid JSON in this exact format, no extra text:
    {{
      "accommodation": {{
        "recommended_type": "e.g. boutique hotel, hostel, homestay",
        "suggested_areas": ["area 1", "area 2"],
        "reasoning": "one or two sentences explaining why this fits the traveler"
      }}
    }}
    """

    response = model.generate_content(prompt)
    parsed, error = parse_llm_json(response.text)

    if error:
        return {
            "accommodation": None,
            "raw_text": response.text,
            "source": "llm",
            "error": error
        }

    return {
        "accommodation": parsed["accommodation"],
        "source": "llm"
    }