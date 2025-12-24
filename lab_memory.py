import os
from mem0 import Memory
from dotenv import load_dotenv

load_dotenv()

# CONFIG: Force Mem0 to use Google Gemini for everything
# This prevents it from asking for an OpenAI key
config = {
    "llm": {
        "provider": "gemini",
        "config": {
            "model": "gemini-flash-latest",
            "temperature": 0.1,
            "max_tokens": 1500,
        }
    },
    "embedder": {
        "provider": "gemini",
        "config": {
            "model": "models/text-embedding-004"
        }
    },
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "riley_memory",
            "path": "db",
        }
    }
}

class RileyMemory:
    def __init__(self):
        # Initialize Mem0 with Gemini Config
        # It will use the GEMINI_API_KEY from your .env automatically
        # (Ensure your .env has GEMINI_API_KEY=AIza...)
        os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
        self.memory = Memory.from_config(config)
        self.user_id = "mark_k"

    def add_interaction(self, user_text, ai_text):
        """Stores a conversation pair into long-term memory"""
        messages = [
            {"role": "user", "content": user_text},
            {"role": "assistant", "content": ai_text}
        ]
        self.memory.add(messages, user_id=self.user_id)
        print(f"🧠 [Memory] Stored: {user_text[:30]}...")

    def recall(self, query):
        """Searches for relevant past facts"""
        print(f"🔍 [Thinking] Searching memory for: '{query}'...")
        results = self.memory.search(query, user_id=self.user_id)
        
        if not results:
            return ""
        
        # Extract the text from the search results
        # Newer Mem0 might return objects or dicts, handling standard dict output
        facts = []
        for res in results:
             if isinstance(res, dict):
                 facts.append(res.get('memory', str(res)))
             else:
                 facts.append(str(res))
                 
        return "\n".join(facts)

# --- TEST LAB ---
if __name__ == "__main__":
    brain = RileyMemory()
    
    # Test 1: Teach her something specific about you
    print("--- Teaching Phase ---")
    brain.add_interaction(
        "My business partner is Chris Gibson. We run KG Media Group.", 
        "Got it. Chris Gibson is your partner at KG Media."
    )
    
    # Test 2: Restart (Simulated) and Recall
    print("\n--- Recall Phase ---")
    fact = brain.recall("Who is my business partner?")
    print(f"✅ RILEY REMEMBERS: {fact}")
