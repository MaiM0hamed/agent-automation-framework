# test_api_key.py
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if api_key:
    # Show only first and last 4 characters for security
    masked = f"{api_key[:8]}...{api_key[-4:]}" if len(api_key) > 12 else "***"
    print(f"[OK] OPENROUTER_API_KEY is set: {masked}")
else:
    print("[ERROR] OPENROUTER_API_KEY is NOT set in .env file")
    print("\nPlease add this line to your .env file:")
    print("OPENROUTER_API_KEY=sk-or-v1-your-actual-key-here")
    print("\nGet your API key from: https://openrouter.ai/keys")
