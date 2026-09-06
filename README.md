# ✈️ Viharam — AI Travel Planning, Without the One-LLM-for-Everything Trap

> Give Viharam a destination, budget, interests, people, and trip duration — and let specialized agents handle the rest.

Viharam is a **multi-agent AI travel planning system** that coordinates different types of logic to build a complete trip plan.

Instead of throwing the entire problem at one giant LLM prompt, Viharam asks a better question: **"What kind of intelligence does each part of the problem actually need?"**

The answer is a combination of **deterministic logic + LLM reasoning + live external data.**

---

## What happens when you plan a trip?

A single trip request can involve:

- 💰 How should the budget be divided?
- 🗓️ What should I do each day?
- 🌦️ What will the weather be like?
- 🏨 Where should I stay?
- 🍜 Where should I eat?
- 🎒 What should I pack?
- 🏖️ What experiences match my interests?

Viharam splits these responsibilities across specialized agents instead of making one LLM do everything.

**One request → multiple specialized agents → one coordinated travel plan.**

---

## Why multi-agent, not one big LLM call?

Not everything needs an LLM.

> ₹50,000 budget + 5 days + 2 people

Calculating allocations doesn't require AI reasoning — it requires **math**.

> "Plan a fun 5-day Goa trip for someone who loves beaches and nightlife."

That involves reasoning, preferences, and pacing — a genuine job for an **LLM**.

> "What's the weather going to be?"

That's a job for a **live weather API**, not an LLM guessing from training data.

**Use the right tool for the right problem.**

---

## Architecture

```text
                         ┌─────────────────────────┐
                         │      TRIP REQUEST       │
                         │   Goa • ₹50K • 5 Days   │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │    COORDINATOR AGENT    │
                         │     Single Entry Point  │
                         └────────────┬────────────┘
                                      │
       ┌──────────────────┬───────────┼───────────┬──────────────────┐
       │                  │           │           │                  │
       ▼                  ▼           ▼           ▼                  ▼
┌──────────────┐  ┌──────────────┐ ┌────────┐ ┌────────────────┐ ┌──────────────┐
│    BUDGET    │  │   ITINERARY  │ │WEATHER │ │ RECOMMENDATION │ │ACCOMMODATION │
│ Deterministic│  │    Gemini    │ │Open-Met│ │     Gemini     │ │    Gemini    │
└──────┬───────┘  └──────┬───────┘ └───┬────┘ └────────┬───────┘ └──────┬───────┘
       │                 │             │               │                │
       └─────────────────┴─────────────┴───────┬───────┴────────────────┘
                                               │
                                               ▼
                                     ┌─────────────────────────┐
                                     │    COMBINED RESPONSE    │
                                     └─────────────────────────┘
```

**Current design:** all five agents run independently off the same trip request. The Coordinator sends each agent the request and combines their outputs — it does not yet pass one agent's output into another. Agent-to-agent negotiation (e.g. Itinerary adjusting plans based on Weather's forecast) is a planned future enhancement, not something currently implemented.

| Agent | Type | Why |
|---|---|---|
| **Budget** | Deterministic (pure Python) | Budget math is arithmetic + threshold checks — no LLM involved, fully auditable logic. |
| **Itinerary** | LLM-driven (Gemini API) | Deciding what to do each day requires reasoning about interests, pacing, and destination. |
| **Weather** | Live external API (Open-Meteo) | Real-world facts, not something an LLM should guess. No API key required. |
| **Recommendation** | LLM-driven (Gemini API) | Suggesting food/experiences/packing tips is reasoning, similar to Itinerary. |
| **Accommodation** | LLM-driven (Gemini API) | Matching stay type/area to budget tier and interests needs contextual reasoning, not a fixed lookup table — pricing and property types vary too much across destinations. |

Every LLM-driven agent labels its output `"source": "llm"`; the Weather agent labels its `"source": "api"`; Budget's output is deterministic and unlabeled by design — so it's always clear which part of a response came from where.

---

## Engineering notes

- All LLM-driven agents (Itinerary, Recommendation, Accommodation) share a single JSON-parsing helper (`agents/utils.py`) instead of duplicating parsing logic — handles cases where the model wraps its response in markdown code fences.
- Every agent has explicit error handling for its own failure mode: `ValueError` for invalid input (Budget), `JSONDecodeError` fallback for malformed LLM output (Itinerary, Recommendation, Accommodation), `RequestException` fallback for network/API failures (Weather). No agent crashes the whole system — each returns a structured error instead.

---

## Tech stack

- Python 3.12
- Google Gemini API (`google-generativeai`)
- Open-Meteo API (weather, no key required)
- `python-dotenv` for API key management

---

## Setup

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

GEMINI_API_KEY=your_key_here

---

## Usage

```python
from agents.coordinator_agent import run_coordinator

trip = {
    "total_budget": 50000,
    "num_days": 5,
    "num_people": 2,
    "destination_tier": "mid",
    "destination": "Goa",
    "interests": ["beaches", "nightlife"]
}

result = run_coordinator(trip)
print(result)
```

---

## 🚧 Status

### ✅ Built & Tested

All **5 core agents** defined in the system architecture are implemented and wired through the Coordinator:

- 💰 **Budget Agent** — deterministic budget allocation
- 🗺️ **Itinerary Agent** — Gemini-powered itinerary generation
- 🌦️ **Weather Agent** — live weather data
- ❤️ **Recommendation Agent** — Gemini-powered recommendations
- 🏨 **Accommodation Agent** — accommodation planning

The complete flow has been **tested end-to-end using real trip data**.

### 🚧 Not Yet Built

The following components from the full system architecture are planned for the next phase:

- **React Frontend + FastAPI Backend** — currently runs as Python scripts with no web layer.
- **Two-Pass Coordinator Flow** — planned flow: task decomposition → agent calls → validation/integration of real-time data. The current Coordinator uses a single-pass flow: it calls all agents and merges their results without a separate validation step.
- **Agent-to-Agent Negotiation** — e.g. letting the Itinerary Agent adjust plans based on the Weather Agent's forecast. Currently, agents operate independently using the same trip request.
- **`requirements.txt`** — one-command dependency installation is planned for the next phase.
- **Edge-Case Input Validation** — validation for cases such as zero or negative values is not yet implemented consistently across all agents.

### 📌 Current Focus

The core agent logic is complete, including the distinction between **Deterministic Logic → LLM Reasoning → Live API Data**.

The next phase focuses on building the surrounding system — frontend, backend, validation, and deeper agent integration.

> Viharam is a final-year academic project, actively in development.