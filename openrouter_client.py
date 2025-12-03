# openrouter_client.py
import os
import json
import httpx
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Any

# Load environment variables
load_dotenv()

class RunResult:
    """Simple result object to mimic agent runner output"""
    def __init__(self, final_output: Any):
        self.final_output = final_output

async def openrouter_chat(prompt: str, model: str = "anthropic/claude-3.5-sonnet", max_tokens: int = 1000) -> str:
    """
    Send a chat request to OpenRouter API.
    
    Args:
        prompt: The user's message/prompt
        model: The model to use (default: anthropic/claude-3.5-sonnet)
        max_tokens: Maximum tokens in the response
        
    Returns:
        The assistant's response text
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables")
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    
    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens
    }
    
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(url, headers=headers, json=data)
        
        # Better error handling
        if response.status_code != 200:
            error_detail = response.text
            print(f"OpenRouter API Error (Status {response.status_code}):")
            print(f"Model: {model}")
            print(f"Response: {error_detail}")
            response.raise_for_status()
        
        result = response.json()
        return result["choices"][0]["message"]["content"]


async def runner_run_openrouter(agent, prompt: str) -> RunResult:
    """
    Run an agent with OpenRouter API.
    
    Args:
        agent: Agent object with name, instructions, model, and output_type
        prompt: The user's prompt
        
    Returns:
        RunResult with final_output containing either parsed object or raw text
    """
    # Combine agent instructions with user prompt
    full_prompt = f"{agent.instructions}\n\n{prompt}"
    
    # Call OpenRouter
    response_text = await openrouter_chat(full_prompt, model=agent.model, max_tokens=2000)
    
    # If agent expects structured output, try to parse it
    if agent.output_type and issubclass(agent.output_type, BaseModel):
        try:
            # Try to extract JSON from response
            # Look for JSON object in the response
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1
            
            if start_idx != -1 and end_idx > start_idx:
                json_str = response_text[start_idx:end_idx]
                parsed_data = json.loads(json_str)
                output = agent.output_type(**parsed_data)
            else:
                raise ValueError("No JSON found in response")
        except Exception as e:
            print(f"Warning: Failed to parse structured output: {e}")
            print(f"Raw response: {response_text}")
            raise
    else:
        # Return raw text
        output = response_text
    
    return RunResult(final_output=output)
