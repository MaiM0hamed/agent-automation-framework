# search_agent.py
from dataclasses import dataclass

@dataclass
class Agent:
    name: str
    instructions: str
    model: str
    output_type: object | None = None

INSTRUCTIONS_SEARCH = (
    "You are a web-search assistant: given a 'Search term' and 'Reason' produce a short web-like summary "
    "with bullets and optionally top-3 urls. Return a plain text answer (no JSON required)."
)

search_agent = Agent(
    name="SearchAgent",
    instructions=INSTRUCTIONS_SEARCH,
    model="openai/gpt-4o-mini",  # Reliable and affordable OpenRouter model
    output_type=None
)
