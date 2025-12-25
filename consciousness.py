import time
import random
from PyQt6.QtCore import QThread, pyqtSignal

# Import your existing lab modules
from lab_senses import AdvancedSenses
from lab_memory import RileyMemory
from lab_subconscious import CuriosityEngine, Librarian, SelfReflection
from lab_soul import RileySoul
from lab_safety import SafetyCore

# Import calendar safely
try:
    from lab_calendar import get_upcoming_events
except ImportError:
    def get_upcoming_events(): 
        return "Calendar Module Offline"

class RileyConsciousness(QThread):
    """
    The Radio-Enabled Brain: Consciousness loop running as a background thread.
    Broadcasts pyqtSignals instead of using print() so the GUI can react.
    """
    # 📡 THE BROADCAST FREQUENCIES (Signals)
    signal_dream_start = pyqtSignal()         # Trigger: Dim Screen
    signal_dream_wake = pyqtSignal()          # Trigger: Undim Screen
    signal_morning_briefing = pyqtSignal(str) # Trigger: Post to Chat
    signal_log_update = pyqtSignal(str)       # Trigger: Update Status Bar

    def __init__(self):
        super().__init__()
        self.senses = AdvancedSenses()
        self.memory = RileyMemory()
        self.subconscious = CuriosityEngine(self.memory)
        self.librarian = Librarian(self.memory)
        self.reflection = SelfReflection(self.memory)
        self.soul = RileySoul(self.memory)
        self.safety = SafetyCore(self.soul)
        
        self.state = "BOOT"
        self.running = True
        self.last_check = 0
        self.last_dream_time = 0

    def run(self):
        """The Main Background Loop"""
        self.signal_log_update.emit("⚡ Nervous System Online")
        
        while self.running:
            # 1. READ SENSES
            idle_time = self.senses.get_idle_time()
            phase = self.senses.get_time_phase()
            
            # 2. STATE MACHINE
            # TEST MODE: 10 seconds idle triggers dream. (Change to 300 for production)
            if idle_time > 10: 
                if self.state != "DREAMING":
                    self.state = "DREAMING"
                    self.signal_dream_start.emit() # <--- FIRE SIGNAL
                    self.signal_log_update.emit("💤 Entering Dream Mode...")
            
                # DREAM LOOP
                if time.time() - self.last_dream_time > 10:
                    self.dream_cycle()
                    self.last_dream_time = time.time()
            
            elif idle_time < 5 and self.state == "DREAMING":
                self.state = "ACTIVE"
                self.signal_dream_wake.emit() # <--- FIRE SIGNAL
                self.signal_log_update.emit(f"☀️ Waking Up ({phase})")
                self.trigger_morning_briefing()

            # 3. MAINTENANCE (Hourly)
            if time.time() - self.last_check > 3600:
                self.run_hourly_maintenance()
                self.last_check = time.time()

            time.sleep(1) # Heartbeat

    def dream_cycle(self):
        """The Subconscious logic with error handling"""
        dice = random.random()
        
        try:
            if dice < 0.3 and self.safety.track_usage("gemini-flash", 500):
                proposal = self.librarian.check_for_mess("test_messy_folder")
                if proposal: 
                    self.soul.grant_xp(5, "Librarian")
                    
            elif dice < 0.5 and self.safety.track_usage("gemini-flash", 1000):
                insight = self.reflection.reflect_on_day()
                if insight: 
                    self.soul.grant_xp(15, "Reflection")

            else:
                if self.safety.track_usage("gemini-flash", 300):
                    thought = self.subconscious.ponder()
                    if thought: 
                        self.soul.grant_xp(10, "Curiosity")
        except Exception as e:
            # Log API errors but don't crash
            self.signal_log_update.emit(f"⚠️ Dream interrupted: {str(e)[:50]}")


    def trigger_morning_briefing(self):
        """Generate morning briefing when waking up"""
        events = get_upcoming_events()
        msg = f"**Welcome back.**\n\n📅 **Schedule:**\n{events}"
        self.signal_morning_briefing.emit(msg)

    def run_hourly_maintenance(self):
        """Periodic maintenance tasks"""
        self.signal_log_update.emit("🧹 Maintenance Cycle")
        
    def stop(self):
        """Gracefully stop the consciousness loop"""
        self.running = False
        self.wait()
