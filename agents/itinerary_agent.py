def generate_itinerary(destination, num_days, interests, destination_tier="mid"):
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    Create a {num_days}-day travel itinerary for {destination}.
    Budget tier: {destination_tier}.
    Traveler interests: {', '.join(interests)}.

    Suggest activities and experiences that fit a {destination_tier}-tier budget —
    avoid luxury-only suggestions for a budget/mid tier, and don't undersell a luxury tier.

    Return ONLY valid JSON in this exact format, no extra text:
    {{
      "itinerary": [
        {{"day": 1, "activities": ["activity 1", "activity 2"]}}
      ]
    }}
    """

    response = model.generate_content(prompt)
    parsed, error = parse_llm_json(response.text)

    if error:
        return {
            "itinerary": None,
            "raw_text": response.text,
            "source": "llm",
            "error": error
        }

    return {
        "itinerary": parsed["itinerary"],
        "source": "llm"
    }