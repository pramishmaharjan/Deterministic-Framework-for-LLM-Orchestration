import os
from pathlib import Path

# Core Paths
BRAIN_ROOT = Path(r"D:\OneDrive\Brains\Work")
BRAIN_OS_ROOT = Path(r"D:\Work\BrainOS")

# Knowledge Base Files
SYSTEM_MD = BRAIN_ROOT / "SYSTEM.md"
MEMORY_MD = BRAIN_ROOT / "MEMORY.md"
CAPABILITY_BRIDGE_MD = BRAIN_ROOT / "capability_bridge.md"
SKILL_BRAIN_MAP_MD = BRAIN_ROOT / "skill_brain_map.md"
SOVEREIGN_STATE_MD = BRAIN_ROOT / "sovereign-state.md"
SEMANTIC_LAYER_MD = BRAIN_ROOT / "Surgical_Semantic_Layer.md"

# DeepAgent Profiles
DEFAULT_HARNESS_PROFILE = "anthropic_opus_4_7"
Surgical_Cores = {
    "L1": {"effort": "standard", "model": "haiku"},
    "L2": {"effort": "high", "model": "sonnet"},
    "L3": {"effort": "xhigh", "model": "sonnet"},
    "L4": {"effort": "max", "model": "opus"},
}

# MCP Endpoints
RUFLO_MCP_ENDPOINT = "stdio" # Assuming ruflo is run as a child process via stdio
