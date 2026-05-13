import os
import subprocess
import sys
from pathlib import Path

def print_header(text):
    print(f"\n{'='*60}\n{text}\n{'='*60}")

def check_python():
    print("[1/5] Checking Python installation...")
    try:
        import sys
        print(f"✅ Python {sys.version.split()[0]} detected.")
    except Exception as e:
        print(f"❌ Python not found: {e}")
        return False
    return True

def install_dependencies():
    print("\n[2/5] Installing Surgical Suite dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully.")
    except Exception as e:
        print(f"❌ Dependency installation failed: {e}")

def setup_brain_structure():
    print("\n[3/5] Initializing local Brain structure...")
    # Default path if the user doesn't specify one in .env
    default_path = Path.home() / "SurgicalBrain" / "Work"

    try:
        default_path.mkdir(parents=True, exist_ok=True)
        # Create essential sub-folders for the deterministic routing to work
        (default_path / "nodes").mkdir(exist_ok=True)
        (default_path / "memory").mkdir(exist_ok=True)
        (default_path / "archives").mkdir(exist_ok=True)

        print(f"✅ Brain structure initialized at: {default_path}")
        print(f"💡 Pro Tip: Update BRAIN_ROOT_PATH in your .env file to this path.")
    except Exception as e:
        print(f"❌ Failed to create brain structure: {e}")

def check_external_tools():
    print("\n[4/5] Verifying external tool integration...")
    tools = {
        "Obsidian": "Required for Knowledge Graphing (Manual Install)",
        "Git": "Required for Version Control",
        "Python": "Surgical Engine Runtime"
    }

    for tool, desc in tools.items():
        print(f"🔍 {tool}: {desc}")

    print("\nNote: Some tools like Obsidian require manual installation.")
    print("Please ensure Obsidian is installed and the 'Surgical Brain' plugin is active.")

def finalize_setup():
    print("\n[5/5] Finalizing setup...")
    if not Path(".env").exists():
        print("⚠️ .env file not found. Creating from .env.example...")
        if Path(".env.example").exists():
            import shutil
            shutil.copy(".env.example", ".env")
            print("✅ .env created. Please edit it with your API keys.")
        else:
            print("❌ .env.example missing. Please create it manually.")
    else:
        print("✅ .env file detected.")

def main():
    print_header("🧠 SURGICAL BRAIN OS - SYSTEM INSTALLER")

    if not check_python():
        print("\n❌ Installation aborted: Python is required.")
        return

    install_dependencies()
    setup_brain_structure()
    check_external_tools()
    finalize_setup()

    print_header("INSTALLATION COMPLETE")
    print("You can now run the system using: python examples/basic_routing.py")

if __name__ == "__main__":
    main()
