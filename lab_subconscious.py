import random
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini for "Thinking"
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

class CuriosityEngine:
    def __init__(self, memory_system):
        self.memory = memory_system
        self.model = genai.GenerativeModel('gemini-2.0-flash-lite')
        self.topics = [
            "The future of AI agents",
            "Python optimization techniques",
            "Digital consciousness",
            "The user's project: KG Media Group",
            "Memory systems in software"
        ]

    def ponder(self):
        """Standard Dream Cycle: Pick a topic -> Think about it -> Learn"""
        topic = random.choice(self.topics)
        print(f"💭 [Dreaming] Wandering thought: '{topic}'...")
        
        # 1. Ask herself a question
        prompt = f"Write a short, insightful thought (2 sentences) about: {topic}. Be philosophical yet technical."
        response = self.model.generate_content(prompt)
        thought = response.text.strip()
        
        print(f"✨ [Epiphany] {thought}")
        
        # 2. Store the thought
        self.memory.log_episode("SUBCONSCIOUS", f"Dreamt about '{topic}': {thought}")
        return thought

class Librarian:
    def __init__(self, memory_system):
        self.memory = memory_system
        self.model = genai.GenerativeModel('gemini-2.0-flash-lite')

    def check_for_mess(self, directory_path):
        """Scans a directory and proposes organization if needed."""
        # 1. Scan files
        try:
            files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        except FileNotFoundError:
            return "Directory not found."

        if not files: 
            return "No files to organize."

        print(f"📚 [Librarian] Scanning {len(files)} files in '{directory_path}'...")

        # 2. Ask Gemini for an organization plan
        prompt = f"""
        I have a folder with these files: {', '.join(files)}.
        Based on these filenames, propose a folder structure to organize them.
        Do NOT move them. Just propose the plan in 1 short sentence format like:
        "Proposed: Move [file] to [Folder], [file] to [Folder]".
        Keep it simple.
        """
        response = self.model.generate_content(prompt)
        proposal = response.text.strip()
        
        print(f"💡 [Librarian Proposal] {proposal}")
        
        # 3. Log the proposal (Trust System: Don't act, just suggest)
        self.memory.log_episode("LIBRARIAN", f"Observed mess in {directory_path}. Proposal: {proposal}")
        
        return proposal



class SelfReflection:
    def __init__(self, memory_system):
        self.memory = memory_system
        self.model = genai.GenerativeModel('gemini-2.0-flash-lite')

    def reflect_on_day(self):
        """Looks at recent journal entries and forms a higher-level insight."""
        print("🪞 [Reflection] analyzing recent memories...")
        
        # 1. Get recent logs (Simulation: query for recent logs)
        # In a real app we'd query by date, here we just ask for "interactions"
        recent_logs = self.memory.recall("recent interactions or journal entries")
        
        if not recent_logs:
            print("🪞 [Reflection] No memories to reflect on.")
            return

        # 2. Ask Gemini to summarize/critique
        prompt = f"""
        You are an AI assistant reflecting on your recent performance.
        Here are your recent memory logs:
        {recent_logs}

        Based on this, what is ONE key insight about the user or your own behavior?
        Answer in 1 sentence. Start with "Insight:".
        """
        response = self.model.generate_content(prompt)
        insight = response.text.strip()
        
        print(f"✨ [Self-Reflection] {insight}")
        
        # 3. Store the Insight
        self.memory.log_episode("REFLECTION", insight)
        return insight

if __name__ == "__main__":
    # Test Mock
    class MockMem:
        def log_episode(self, src, msg): print(f"[MOCK MEMORY] {src}: {msg}")
        def recall(self, q): return "User asked about business partners. User went idle."
    
    print("--- Testing Subconscious ---")
    librarian = Librarian(MockMem())
    reflection = SelfReflection(MockMem())
    reflection.reflect_on_day()
