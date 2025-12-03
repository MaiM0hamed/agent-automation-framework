# deep_research.py
import asyncio
from research_manager import run_query_and_print

if __name__ == "__main__":
    query = "Latest approaches to autonomous navigation for visually impaired people 2024"
    asyncio.run(run_query_and_print(query))
