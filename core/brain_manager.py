import os
from pathlib import Path

class BrainManager:
    """
    Handles the dynamic creation and resolution of the Brain Root Path.
    Ensures the framework operates on the D: drive for Windows users, 
    falling back to home directory on other platforms.
    """
    DEFAULT_FOLDER_NAME = "Deterministic-Framework-Brain"

    @classmethod
    def get_brain_root(cls) -> str:
        # 1. Check environment variable first
        env_path = os.getenv("BRAIN_ROOT_PATH")
        if env_path:
            return env_path

        # 2. Try to use D: drive on Windows
        if os.name == 'nt':
            d_drive_path = Path("D:/") / cls.DEFAULT_FOLDER_NAME
            try:
                if not d_drive_path.exists():
                    d_drive_path.mkdir(parents=True, exist_ok=True)
                return str(d_drive_path)
            except (PermissionError, OSError):
                # Fallback if D: is not available or writable
                pass

        # 3. Fallback to home directory
        home_path = Path.home() / cls.DEFAULT_FOLDER_NAME
        home_path.mkdir(parents=True, exist_ok=True)
        return str(home_path)

    @classmethod
    def initialize_brain_structure(cls):
        """Creates the minimal required directory structure for the brain."""
        root = cls.get_brain_root()
        root_path = Path(root)
        
        required_dirs = [
            "nodes",
            "memory",
            "kernels",
            "weights"
        ]
        
        for folder in required_dirs:
            (root_path / folder).mkdir(parents=True, exist_ok=True)
        
        # Create minimal sample weights
        weights_file = root_path / "weights" / "routing_weights.json"
        if not weights_file.exists():
            weights_file.write_text('{"L1": 0.1, "L2": 0.2, "L3": 0.3, "L4": 0.4}')
            
        # Create minimal sample kernels
        kernels_dir = root_path / "kernels"
        if not (kernels_dir / "base_kernel.txt").exists():
            (kernels_dir / "base_kernel.txt").write_text("Surgical Brain Kernel: Process input with absolute precision.")

        return root
