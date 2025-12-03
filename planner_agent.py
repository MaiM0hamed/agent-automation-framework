# planner_agent.py
from pydantic import BaseModel
from typing import List
from dataclasses import dataclass

class WebSearchItem(BaseModel):
    reason: str
    query: str

class WebSearchPlan(BaseModel):
    searches: List[WebSearchItem]

@dataclass
class Agent:
    name: str
    instructions: str
    model: str
    output_type: object | None = None

# Instructions example (you can edit)
HOW_MANY_SEARCHES = 3
INSTRUCTIONS_PLANNER = (
    f"You are a helpful research assistant. Given a query, produce exactly {HOW_MANY_SEARCHES} web search items.\n"
    "Return a JSON object exactly in this form: {\"searches\": [{\"reason\":\"...\",\"query\":\"...\"}, ...]} and nothing else."
)

planner_agent = Agent(
    name="PlannerAgent",
    instructions=INSTRUCTIONS_PLANNER,
    model="openai/gpt-4o-mini",  # Reliable and affordable OpenRouter model
    output_type=WebSearchPlan
)
