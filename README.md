# ✈️ Viharam — AI Travel Planning, Without the One-LLM-for-Everything Trap

> **Give Viharam a destination, budget, interests, people, and trip duration — and let specialized agents handle the rest.**

Viharam is a **multi-agent AI travel planning system** that coordinates different types of logic to build a complete trip plan.

Instead of throwing the entire problem at one giant LLM prompt, Viharam asks a better question:

**“What kind of intelligence does each part of the problem actually need?”**

The answer is a combination of **deterministic logic + LLM reasoning + live external data.**

---

## 🌍 What happens when you plan a trip?

A single trip request can involve:

💰 How should the budget be divided?  
🗓️ What should I do each day?  
🌦️ What will the weather be like?  
🍜 Where should I eat?  
🎒 What should I pack?  
🏖️ What experiences match my interests?

Viharam splits these responsibilities across specialized agents instead of making one LLM do everything.

### The result?

**One request → multiple specialized agents → one coordinated travel plan.**

---

## 🧠 Why Multi-Agent AI?

Because **not everything needs an LLM.**

For example:

> ₹50,000 budget + 5 days + 2 people

Calculating allocations doesn't require AI reasoning.

It requires **math.**

On the other hand:

> “Plan a fun 5-day Goa trip for someone who loves beaches and nightlife.”

That involves **reasoning, preferences, pacing, and context** — a much better job for an LLM.

And:

> “What's the weather going to be?”

That's a job for a **live weather API**, not an LLM guessing from its training data.

### Viharam follows one simple principle:

**Use the right tool for the right problem.**

---

# 🏗️ Architecture

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
              ┌───────────────────────┼───────────────────────┐
              │                       │                       │
              ▼                       ▼                       ▼
     ┌────────────────┐      ┌────────────────┐      ┌────────────────┐
     │      BUDGET    │      │    ITINERARY   │      │     WEATHER    │
     │  Deterministic │      │     Gemini     │      │   Open-Meteo   │
     └───────┬────────┘      └───────┬────────┘      └───────┬────────┘
             │                       │                       │
             │                       │                       │
             │               ┌────────────────┐              │
             │               │ RECOMMENDATION │              │
             │               │     Gemini     │              │
             │               └───────┬────────┘              │
             │                       │                       │
             └───────────────────────┼───────────────────────┘
                                     │
                                     ▼
                         ┌─────────────────────────┐
                         │    COMBINED RESPONSE    │
                         └─────────────────────────┘

## Setup

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_key_here
```

### 🔥 Why I REALLY like that last block

It protects you from a panel question like:

> **“Does your Recommendation Agent receive the Itinerary Agent's output?”**

You can confidently say:

> **“No. In the current version, the agents operate independently. The Coordinator sends them the same trip request and combines their outputs. Agent-to-agent negotiation is a planned future enhancement, not something I'm claiming to have implemented.”**

That's actually **better engineering communication** than pretending the system is more advanced than it is.

And your README's strongest story is now very clear:

**Deterministic logic → where arithmetic is enough**  
**LLM → where reasoning is needed**  
**API → where live external facts are needed**  
**Coordinator → orchestration, not fake agent-to-agent intelligence**

                        