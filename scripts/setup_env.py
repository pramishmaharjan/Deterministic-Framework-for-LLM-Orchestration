import os
import subprocess
import sys
from pathlib import Path

def main():
    print("\n🧠 SURGICAL BRAIN OS - SYSTEM INSTALLER")
    # Python check
    print("[1/5] Checking Python...")
    # Dependencies
    print("[2/5] Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    # Brain structure
    print("[3/5] Initializing local Brain structure...")
    default_path = Path.home() / "SurgicalBrain" / "Work"
    default_path.mkdir(parents=True, exist_ok=True)
    (default_path / "nodes").mkdir(exist_ok=True)
    (default_path / "memory").mkdir(exist_ok=True)
    # Environment
    print("[4/5] Configuring environment...")
    if not Path(".env").exists():
        import shutil
        shutil.copy(".env.example", ".env")
    print("\n✅ INSTALLATION COMPLETE")

if __name__ == "__main__":
    main()
