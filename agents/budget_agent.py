def calculate_budget(total_budget, num_days, num_people, destination_tier="mid"):
    min_per_day_per_person = {
        "budget": 800,
        "mid": 2000,
        "luxury": 5000
    }

    destination_tier = destination_tier.lower().strip()

    if destination_tier not in min_per_day_per_person:
        raise ValueError(f"Invalid tier '{destination_tier}'. Choose from: budget, mid, luxury")

    min_required = min_per_day_per_person[destination_tier] * num_days * num_people

    feasible = total_budget >= min_required
    warning = None
    if not feasible:
        warning = f"Budget too low for {destination_tier} tier: need at least ₹{min_required}, got ₹{total_budget}"

    daily_budget = total_budget / num_days

    allocation = {
        "accommodation": round(total_budget * 0.40),
        "food": round(total_budget * 0.20),
        "transport": round(total_budget * 0.20),
        "activities": round(total_budget * 0.15),
        "buffer": round(total_budget * 0.05),
    }

    return {
        "daily_budget": round(daily_budget),
        "allocation": allocation,
        "feasible": feasible,
        "warning": warning
    }
