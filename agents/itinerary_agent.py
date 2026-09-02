import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_itinerary(destination, num_days, interests):
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    Create a {num_days}-day travel itinerary for {destination}.
    Traveler interests: {', '.join(interests)}.

    Return ONLY valid JSON in this exact format, no extra text:
    {{
      "itinerary": [
        {{"day": 1, "activities": ["activity 1", "activity 2"]}}
      ]
    }}
    """

    response = model.generate_content(prompt)
    cleaned_text = response.text.strip()

    if cleaned_text.startswith("```"):
        cleaned_text = cleaned_text.split("```")[1]
        if cleaned_text.startswith("json"):
            cleaned_text = cleaned_text[4:]
        cleaned_text = cleaned_text.strip()

    try:
        parsed = json.loads(cleaned_text)
        return {
            "itinerary": parsed["itinerary"],
            "source": "llm"
        }
    except json.JSONDecodeError:
        return {
            "itinerary": None,
            "raw_text": response.text,
            "source": "llm",
            "error": "Failed to parse LLM response as JSON"
        }