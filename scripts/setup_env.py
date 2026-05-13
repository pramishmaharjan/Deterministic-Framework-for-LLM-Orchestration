import os
import subprocess
import sys
from pathlib import Path

def main():
    print("\n🧠 SURGICAL BRAIN OS - SYSTEM INSTALLER")
    # Python check
    print("[1/5] Checking Python...")
    # Dependencies
    print("[2/ la 5] Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    # Brain structure
    print("[3/ la 5] Initializing dynamic Brain structure...")
    from core.brain_manager import BrainManager
    brain_path = BrainManager.initialize_brain_structure()
    print(f"Brain initialized at: {brain_path}")
    # Environment
    print("[4/ la 5] Configuring environment...")
    if not Path(".env").exists():
        import shutil
        shutil.copy(".env.example", ".env")
    print("\n✅ INSTALLATION COMPLETE")

if __name__ == "__main__":
    main()
