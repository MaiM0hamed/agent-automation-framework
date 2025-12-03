# openrouter_test.py
import asyncio
from openrouter_client import openrouter_chat

async def main():
    out = await openrouter_chat("Write a one-line summary of the latest AI news.", model="anthropic/claude-opus-4.5", max_tokens=120)
    print(out)

if __name__ == "__main__":
    asyncio.run(main())
