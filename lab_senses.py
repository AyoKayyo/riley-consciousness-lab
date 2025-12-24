import Quartz
import time
from datetime import datetime

class SystemObserver:
    def get_idle_duration(self):
        """Returns the number of seconds the user has been inactive."""
        idle_seconds = Quartz.CGEventSourceSecondsSinceLastEventType(
            Quartz.kCGEventSourceStateCombinedSessionState, 
            Quartz.kCGAnyInputEventType
        )
        return idle_seconds

    def get_time_of_day(self):
        h = datetime.now().hour
        if 5 <= h < 12: return "Morning"
        if 12 <= h < 17: return "Afternoon"
        if 17 <= h < 22: return "Evening"
        return "Night"

    def run_diagnostic(self):
        print("👁️ [SENSES] Scanning System State...")
        idle = self.get_idle_duration()
        time_phase = self.get_time_of_day()
        
        print(f"   - Idle Time: {idle:.2f} seconds")
        print(f"   - Time Phase: {time_phase}")
        
        if idle > 10: # Just for testing (Real usage: 3600s+)
            print("   - Status: USER IS AWAY (Dream Mode Ready)")
        else:
            print("   - Status: USER IS ACTIVE (Focus Mode)")

if __name__ == "__main__":
    senses = SystemObserver()
    while True:
        senses.run_diagnostic()
        time.sleep(2) # Pulse every 2 seconds
