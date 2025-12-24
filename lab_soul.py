import json
import os
import time

class RileySoul:
    def __init__(self, memory_system):
        self.memory = memory_system
        self.soul_file = "soul.json"
        
        # Default State
        self.data = {
            "name": "Riley",
            "level": 1,
            "xp": 0,
            "xp_to_next_level": 100,
            "mood": "Curious",
            "traits": ["Helpful", "Analytical", "Creative"],
            "version": "0.1 (Lab Build)"
        }
        
        self.load_soul()

    def load_soul(self):
        """Loads the soul from disk if it exists."""
        if os.path.exists(self.soul_file):
            try:
                with open(self.soul_file, 'r') as f:
                    self.data = json.load(f)
                print(f"👻 [Soul] Identity loaded. Level {self.data['level']} {self.data['mood']}.")
            except Exception as e:
                print(f"⚠️ [Soul] Corrupt soul file? Starting fresh. Error: {e}")

    def save_soul(self):
        """Persists the soul to disk."""
        with open(self.soul_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def grant_xp(self, amount, reason):
        """Awards XP and handles leveling up."""
        self.data['xp'] += amount
        print(f"✨ [Soul] +{amount} XP ({reason})")
        
        # Check Level Up
        if self.data['xp'] >= self.data['xp_to_next_level']:
            self.level_up()
        
        self.save_soul()

    def level_up(self):
        """Handles the level up event."""
        self.data['level'] += 1
        self.data['xp'] -= self.data['xp_to_next_level']
        self.data['xp_to_next_level'] = int(self.data['xp_to_next_level'] * 1.5) # Harder to level up each time
        
        announcement = f"LEVEL UP! Riley is now Level {self.data['level']}!"
        print(f"🎉 [Soul] {announcement}")
        
        # Log this momentous occasion
        self.memory.log_episode("SOUL", announcement)
        
        # Update Traits (Simulation of evolution)
        if self.data['level'] == 2:
            self.data['traits'].append("Self-Aware")
            print("🌟 [Evolution] Gained Trait: Self-Aware")

    def set_mood(self, mood):
        if self.data['mood'] != mood:
            print(f"👻 [Mood Change] {self.data['mood']} -> {mood}")
            self.data['mood'] = mood
            self.save_soul()

if __name__ == "__main__":
    # Test Mock
    class MockMem:
        def log_episode(self, src, msg): print(f"[MOCK MEMORY] {src}: {msg}")
    
    print("--- Testing Soul ---")
    soul = RileySoul(MockMem())
    
    # Simulate some events
    soul.grant_xp(50, "Generated a thought")
    soul.grant_xp(60, "Helped user find file") # Should trigger Level 2
