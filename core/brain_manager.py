import os
from pathlib import Path

class BootError(Exception):
    """Raised when the Brain's boot sequence fails a critical check."""
    pass

class BrainManager:
    """
    Handles the dynamic creation and resolution of the Brain Root Path.
    Ensures the framework operates on the D: drive for Windows users,
    falling back to home directory on other platforms.
    """
    DEFAULT_ROOT = "D:/OneDrive/Brains/Work"
    DEFAULT_FOLDER_NAME = "Deterministic-Framework-Brain"

    @classmethod
    def get_brain_root(cls) -> str:
        # 1. Check environment variable first
        env_path = os.getenv("BRAIN_ROOT_PATH")
        if env_path:
            return env_path

        # 2. Prioritize the Surgical Brain OS path on Windows
        if os.name == 'nt':
            if Path(cls.DEFAULT_ROOT).exists():
                return cls.DEFAULT_ROOT

            # Fallback to the previously used default folder on D:
            d_drive_path = Path("D:/") / cls.DEFAULT_FOLDER_NAME
            try:
                if not d_drive_path.exists():
                    d_drive_path.mkdir(parents=True, exist_ok=True)
                return str(d_drive_path)
            except (PermissionError, OSError):
                pass

        # 3. Fallback to home directory
        home_path = Path.home() / cls.DEFAULT_FOLDER_NAME
        home_path.mkdir(parents=True, exist_ok=True)
        return str(home_path)

    @classmethod
    def perform_symmetry_check(cls, brain_root: str, active_skills: list[str]):
        """Verifies that active skills align with the brain's skill_brain_map.md."""
        map_path = Path(brain_root) / "wiki" / "skill_brain_map.md"
        if not map_path.exists():
            # If the map is missing, we warn but don't halt unless strict mode is on
            print(f"Warning: Symmetry map not found at {map_path}")
            return True

        content = map_path.read_text()
        for skill in active_skills:
            if skill not in content:
                print(f"Symmetry Error: Skill '{skill}' is active but not mapped in brain.")
                return False
        return True

    @classmethod
    def boot_sequence(cls, active_skills: list[str] = None):
        """
        The mandatory heartbeat check before any operation.
        1. Path Verification -> 2. Index Loading -> 3. Symmetry Check.
        """
        root = cls.get_brain_root()
        root_path = Path(root)

        # 1. Path Verification
        if not root_path.exists():
            raise BootError(f"Critical Path missing: {root}")

        # 2. Index Loading (simulated check for index.json or MEMORY.md)
        index_file = root_path / "index.json"
        memory_file = root_path / "MEMORY.md"
        if not index_file.exists() and not memory_file.exists():
            print("Warning: Brain index not found. Operating in limited discovery mode.")

        # 3. Symmetry Check
        if active_skills is not None:
            if not cls.perform_symmetry_check(root, active_skills):
                raise BootError("Symmetry Check failed: Active skills do not align with Brain nodes.")

        return root

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
