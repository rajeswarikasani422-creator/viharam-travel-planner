import json

def parse_llm_json(raw_text):
    cleaned_text = raw_text.strip()

    if cleaned_text.startswith("```"):
        cleaned_text = cleaned_text.split("```")[1]
        if cleaned_text.startswith("json"):
            cleaned_text = cleaned_text[4:]
        cleaned_text = cleaned_text.strip()

    try:
        return json.loads(cleaned_text), None
    except json.JSONDecodeError:
        return None, "Failed to parse LLM response as JSON"