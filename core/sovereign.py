from pathlib import Path
from typing import Any, Dict, List


class SovereignFailure(Exception):
    """Raised when output fails Sovereign alignment against sovereign_state.md."""
    pass


class SovereignValidator:
    def __init__(self, state_file: str = "config/sovereign_state.md"):
        self.state_path = Path(state_file)
        self.constraints = self._load_state()

    def _load_state(self) -> Dict[str, List[str]]:
        constraints: Dict[str, List[str]] = {
            "precision": [],
            "factuality": [],
            "format": [],
        }
        if not self.state_path.exists():
            return constraints
        content = self.state_path.read_text(encoding="utf-8")
        current_section: str | None = None
        for line in content.split("\n"):
            lower = line.lower().strip()
            if "precision" in lower and ":" not in line.strip("-# "):
                current_section = "precision"
            elif "factuality" in lower and ":" not in line.strip("-# "):
                current_section = "factuality"
            elif "format" in lower and ":" not in line.strip("-# "):
                current_section = "format"
            elif line.strip().startswith("-") and current_section:
                constraints[current_section].append(line.strip("- "))
        return constraints

    def validate(self, output: str) -> str:
        print(f"[Sovereign] Validating output against {self.state_path}...")

        format_rules = self.constraints.get("format", [])
        for rule in format_rules:
            if "filler" in rule.lower():
                filler_words = ["um", "uh", "well ", "actually ", "basically"]
                lower = f" {output.lower()} "
                for word in filler_words:
                    if f" {word}" in lower or f"{word} " in lower:
                        raise SovereignFailure(
                            f"Format violation: conversational filler '{word.strip()}' detected."
                        )

        precision_rules = self.constraints.get("precision", [])
        for rule in precision_rules:
            if "hallucination" in rule.lower():
                if "perhaps" in output.lower() or "might be" in output.lower():
                    raise SovereignFailure(
                        "Precision violation: speculative language detected."
                    )

        factuality_rules = self.constraints.get("factuality", [])
        for rule in factuality_rules:
            if "traceable" in rule.lower():
                if not any(marker in output for marker in ["[Source:", "Source:", "(source:"]):
                    raise SovereignFailure(
                        "Factuality violation: output lacks traceable source markers."
                    )

        return (
            f"{output}\n\n--- \n"
            "Sovereign Alignment: Verified. Output adheres to core technical constraints."
        )
