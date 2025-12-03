# writer_agent.py
from dataclasses import dataclass

@dataclass
class Agent:
    name: str
    instructions: str
    model: str
    output_type: object | None = None

INSTRUCTIONS_WRITER = (
    "You are a concise research writer. Given aggregated search results, produce a structured ~300 word summary "
    "with: 1) TL;DR (one-line), 2) Key findings (3 bullets), 3) Recommended next steps (2 bullets). Return plain text."
)

writer_agent = Agent(
    name="WriterAgent",
    instructions=INSTRUCTIONS_WRITER,
    model="openai/gpt-4o-mini",  # Reliable and affordable OpenRouter model
    output_type=None
)
