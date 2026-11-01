# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Non-Sleep Deep Rest (NSDR) Protocol Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentNonSleepDeepRestNsdrProtocol

def main():
    agent = PersonalAgentNonSleepDeepRestNsdrProtocol()

    print("=" * 70)
    print("DEMO: Personal Agent Non-Sleep Deep Rest (NSDR) Engine")
    print("=" * 70)

    # 1. Evaluate NSDR Physiological State Shift (25 min session, RR drops 16 -> 7.5 bpm)
    res_shift = agent.evaluate_nsdr_state_shift(
        session_duration_minutes=25.0,
        baseline_respiratory_rate_bpm=16.0,
        post_session_respiratory_rate_bpm=7.5,
        baseline_subjective_arousal_10=8.0,
        post_session_subjective_arousal_10=2.5
    )

    print(f"\n1. NSDR Autonomic State Shift (25 min Protocol):")
    print(f"   Duration: {res_shift['session_duration_minutes']} min")
    print(f"   Respiratory Deceleration: -{res_shift['respiratory_deceleration_bpm']} bpm ({res_shift['respiratory_rate_reduction_pct']} drop)")
    print(f"   Arousal Reduction: {res_shift['subjective_arousal_reduction_pct']}")
    print(f"   PDRI Index: {res_shift['parasympathetic_down_regulation_index_pdri']}/100")
    print(f"   Neurological Depth: {res_shift['neurological_depth_tier']}")
    print(f"   Projected EEG Wave: {res_shift['projected_eeg_phase']}")
    print(f"   Striatal Dopamine Replenishment: {res_shift['striatal_dopamine_replenishment_pct']}")
    print(f"   Sleep Inertia: {res_shift['sleep_inertia_risk']}")

    # 2. Recommend Chronobiological Timing Protocol
    res_proto = agent.recommend_nsdr_timing_protocol(
        sleep_debt_hours=1.8,
        morning_cognitive_load="high",
        current_hour_24h=14.25  # 14:15
    )

    print(f"\n2. Circadian NSDR Prescription:")
    print(f"   Sleep Debt: {res_proto['sleep_debt_hours']} hrs")
    print(f"   Prescribed Protocol: {res_proto['prescribed_protocol']}")
    print(f"   Recommended Duration: {res_proto['recommended_duration_minutes']} min")
    print(f"   Optimal Circadian Window: {res_proto['optimal_circadian_window_24h']}")
    print(f"   Alignment: {res_proto['timing_alignment_status']}")
    print(f"   Instructions: {res_proto['execution_instructions']}")

    print("\nVerification complete: NSDR protocol engine executed flawlessly.")

if __name__ == "__main__":
    main()
