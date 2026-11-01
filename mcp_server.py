# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Non-Sleep Deep Rest (NSDR) Protocol Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentNonSleepDeepRestNsdrProtocol

mcp = FastMCP("PersonalAgentNonSleepDeepRestNsdrProtocol")
client = PersonalAgentNonSleepDeepRestNsdrProtocol()

@mcp.tool()
def evaluate_nsdr_state_shift(
    session_duration_minutes: float = 20.0,
    baseline_respiratory_rate_bpm: float = 16.0,
    post_session_respiratory_rate_bpm: float = 8.5,
    baseline_subjective_arousal_10: float = 7.5,
    post_session_subjective_arousal_10: float = 3.0
) -> str:
    """Calculates Parasympathetic Down-Regulation Index (PDRI), dopamine replenishment, and EEG depth."""
    import json
    return json.dumps(client.evaluate_nsdr_state_shift(
        session_duration_minutes, baseline_respiratory_rate_bpm, post_session_respiratory_rate_bpm,
        baseline_subjective_arousal_10, post_session_subjective_arousal_10
    ), indent=2)

@mcp.tool()
def recommend_nsdr_timing_protocol(
    sleep_debt_hours: float = 1.5,
    morning_cognitive_load: str = "high",
    current_hour_24h: float = 14.0
) -> str:
    """Prescribes ideal NSDR duration and execution window based on circadian nadir and sleep debt."""
    import json
    return json.dumps(client.recommend_nsdr_timing_protocol(
        sleep_debt_hours, morning_cognitive_load, current_hour_24h
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
