# research_manager.py
import asyncio
from openrouter_client import runner_run_openrouter
from planner_agent import planner_agent, WebSearchPlan
from search_agent import search_agent
from writer_agent import writer_agent
from types import SimpleNamespace

class ResearchManager:
    async def run(self, query: str) -> str:
        # 1) Plan
        plan_res = await runner_run_openrouter(planner_agent, f"Query: {query}")
        plan = plan_res.final_output  # WebSearchPlan object
        if not isinstance(plan, WebSearchPlan):
            raise RuntimeError("Planner did not return a valid WebSearchPlan")

        # 2) Perform searches in parallel
        tasks = [asyncio.create_task(self._run_search_item(item)) for item in plan.searches]
        results = await asyncio.gather(*tasks)

        # 3) Aggregate results
        combined = "\n\n".join([
            f"=== Search: {r['query']} ===\nReason: {r['reason']}\n\n{r['search_result']}"
            for r in results
        ])

        # 4) Write final summary using writer agent
        writer_res = await runner_run_openrouter(writer_agent, f"Aggregated results:\n\n{combined}")
        final_text = writer_res.final_output  # raw text summary
        return final_text

    async def _run_search_item(self, item):
        res = await runner_run_openrouter(search_agent, f"Search term: {item.query}\nReason: {item.reason}")
        return {"query": item.query, "reason": item.reason, "search_result": res.final_output}

# helper to run from script
async def run_query_and_print(query: str):
    rm = ResearchManager()
    out = await rm.run(query)
    print("\n=== FINAL SUMMARY ===\n")
    print(out)
