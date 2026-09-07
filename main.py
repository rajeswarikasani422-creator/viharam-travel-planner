from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from agents.coordinator_agent import run_coordinator

app = FastAPI(title="Viharam API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TripRequest(BaseModel):
    total_budget: float
    num_days: int
    num_people: int
    destination: str
    destination_tier: Optional[str] = "mid"
    interests: Optional[List[str]] = []

@app.get("/")
def health_check():
    return {"status": "Viharam API is running"}

@app.post("/plan-trip")
def plan_trip(trip: TripRequest):
    trip_request = trip.model_dump()
    result = run_coordinator(trip_request)
    return result