import time
import asyncio
from lab_senses import SystemObserver
from lab_memory import RileyMemory
# Import calendar only if you have the credentials, otherwise use dummy
try:
    from lab_calendar import get_upcoming_events
except ImportError:
    def get_upcoming_events(): return "Calendar Module Offline"

class RileyConsciousness:
    def __init__(self):
        self.senses = SystemObserver()
        self.memory = RileyMemory()
        self.state = "BOOT"
        self.last_check = 0

    def run_loop(self):
        print("⚡ [SYSTEM] Riley Nervous System Online")
        print("   - Monitoring Idle Time")
        print("   - Memory Core Active")
        
        while True:
            # 1. READ SENSES
            idle_time = self.senses.get_idle_duration()
            phase = self.senses.get_time_of_day()
            
            # 2. DECIDE STATE
            if idle_time > 300: # 5 Minutes Idle
                if self.state != "DREAMING":
                    print("💤 [State Change] User Away. Entering Dream Mode...")
                    self.state = "DREAMING"
                    # Here is where she would read files/learn in background
            
            elif idle_time < 5 and self.state == "DREAMING":
                print(f"☀️ [State Change] User Returned! Good {phase}.")
                self.state = "ACTIVE"
                self.trigger_morning_briefing()

            # 3. PULSE CHECK (Every 1 hour)
            if time.time() - self.last_check > 3600:
                self.run_hourly_maintenance()
                self.last_check = time.time()

            time.sleep(2) # Heartbeat

    def trigger_morning_briefing(self):
        """Called when you wake up the computer"""
        events = get_upcoming_events()
        # We don't print this, we would ideally inject it into the Chat UI
        # For now, we print to console to prove it works
        print(f"\n🔔 [NOTIFICATION] Welcome back, Mark.")
        print(f"   Here is your schedule:\n{events}\n")

    def run_hourly_maintenance(self):
        print("🧹 [MAINTENANCE] Organizing memories...")

if __name__ == "__main__":
    os = RileyConsciousness()
    os.run_loop()
