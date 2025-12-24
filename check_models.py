import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    # try getting from GOOGLE_API_KEY if GEMINI_API_KEY is not set
    api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ No API Key found.")
    exit(1)

client = genai.Client(api_key=api_key)
print("Using API Key starting with:", api_key[:4] + "...")

try:
    print("Fetching models...")
    # The new SDK syntax for listing models might differ, attempting standard way
    # Based on error message "Call ListModels"
    models = client.models.list(config={"query_base": True}) 
    # Or iterate
    for m in models:
        print(f"- {m.name}")
except Exception as e:
    print(f"Error listing models: {e}")
    # Try alternate method if new SDK differs
    try:
         import google.generativeai as genai_old
         genai_old.configure(api_key=api_key)
         for m in genai_old.list_models():
             print(f"[Old SDK] {m.name}")
    except Exception as e2:
         print(f"Old SDK fallback failed: {e2}")
