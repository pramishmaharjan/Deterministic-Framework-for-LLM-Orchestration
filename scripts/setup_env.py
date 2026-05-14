import os
import subprocess
import sys
from pathlib import Path

# Ensure the root directory is in sys.path so core can be imported
root_dir = Path(__file__).parent.parent.absolute()
sys.path.append(str(root_dir))

def main():
    print("\n--- SURGICAL BRAIN OS - SYSTEM INSTALLER ---")

    # 1. Dependencies
    print("[1/4] Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    # 2. Environment Configuration
    print("[2/4] Configuring environment...")
    if not Path(".env").exists():
        import shutil
        shutil.copy(".env.example", ".env")
        print("Created .env from .env.example")

    from dotenv import load_dotenv
    load_dotenv()

    # 3. Brain Structure
    print("[3/4] Initializing dynamic Brain structure...")
    from core.brain_manager import BrainManager
    brain_path = BrainManager.initialize_brain_structure()
    print(f"Brain initialized at: {brain_path}")

    # 4. Final Verification
    print("[4/4] Verifying system integrity...")
    if Path(brain_path).exists():
        print("\nINSTALLATION COMPLETE")
        print(f"Your Brain is live at: {brain_path}")
    else:
        print("\nInstallation failed: Could not create Brain directory.")


if __name__ == "__main__":
    main()
