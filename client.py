# -*- coding: utf-8 -*-
"""Personal Agent Non-Sleep Deep Rest (NSDR) Protocol Skill.

Zero-dependency NSDR / Yoga Nidra neuro-autonomic state shift modeler,
alpha/theta entrainment window projector, and striatal dopamine replenishment estimator.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentNonSleepDeepRestNsdrProtocol:
    """Quantitative neuro-autonomic down-regulation and cognitive restoration modeler
    based on the Non-Sleep Deep Rest (NSDR) / Yoga Nidra paradigm."""

    def evaluate_nsdr_state_shift(
        self,
        session_duration_minutes: float = 20.0,
        baseline_respiratory_rate_bpm: float = 16.0,
        post_session_respiratory_rate_bpm: float = 8.5,
        baseline_subjective_arousal_10: float = 7.5,
        post_session_subjective_arousal_10: float = 3.0
    ) -> Dict[str, Any]:
        """Calculates Parasympathetic Down-Regulation Index (PDRI), striatal dopamine reserve
        replenishment, and electroencephalographic phase depth."""
        dur = max(5.0, min(60.0, float(session_duration_minutes)))
        rr_base = max(10.0, float(baseline_respiratory_rate_bpm))
        rr_post = max(4.0, float(post_session_respiratory_rate_bpm))
        arousal_base = max(0.0, min(10.0, float(baseline_subjective_arousal_10)))
        arousal_post = max(0.0, min(10.0, float(post_session_subjective_arousal_10)))

        delta_rr = max(0.0, rr_base - rr_post)
        rr_reduction_pct = round((delta_rr / rr_base) * 100.0, 1)

        delta_arousal = max(0.0, arousal_base - arousal_post)
        arousal_reduction_pct = round((delta_arousal / max(1.0, arousal_base)) * 100.0, 1)

        # Parasympathetic Down-Regulation Index (PDRI: 0 - 100)
        # Duration weight: optimal between 15-30 mins
        duration_efficiency = 1.0 if (15.0 <= dur <= 35.0) else (0.8 if dur < 15.0 else 0.85)
        pdri = min(100.0, round(((delta_rr * 4.5) + (delta_arousal * 6.5)) * duration_efficiency, 1))

        # Striatal Dopamine Replenishment Estimate
        # Kjaer et al. 2002 demonstrated up to ~65% surge in 11C-raclopride striatal dopamine availability
        dopamine_recovery_pct = round(min(65.0, (dur / 30.0) * 45.0 * (pdri / 80.0)), 1)

        # EEG Brainwave Phase Attained
        if dur >= 20.0 and pdri >= 65.0:
            eeg_phase = "Theta Wave Hypnagogic Baseline (4 - 7 Hz) / Conscious Rest"
            depth_tier = "Deep Somatosensory Dissociation / Optimal Synaptic Reset"
        elif dur >= 10.0 and pdri >= 40.0:
            eeg_phase = "Alpha Wave Relaxation (8 - 12 Hz)"
            depth_tier = "Moderate Cortical Calming / Attenuated Beta Chatter"
        else:
            eeg_phase = "High Beta / Superficial Somatic Calming (> 13 Hz)"
            depth_tier = "Incipient Down-Regulation / Residual Cognitive Friction"

        return {
            "session_duration_minutes": dur,
            "respiratory_deceleration_bpm": round(delta_rr, 1),
            "respiratory_rate_reduction_pct": f"{rr_reduction_pct}%",
            "subjective_arousal_reduction_pct": f"{arousal_reduction_pct}%",
            "parasympathetic_down_regulation_index_pdri": pdri,
            "neurological_depth_tier": depth_tier,
            "projected_eeg_phase": eeg_phase,
            "striatal_dopamine_replenishment_pct": f"+{dopamine_recovery_pct}%",
            "sleep_inertia_risk": "Zero (Maintains full prefrontal lucidity upon completion)" if dur <= 30.0 else "Mild (< 10 min)"
        }

    def recommend_nsdr_timing_protocol(
        self,
        sleep_debt_hours: float,
        morning_cognitive_load: str = "high",
        current_hour_24h: float = 14.0
    ) -> Dict[str, Any]:
        """Prescribes ideal NSDR duration and execution window based on circadian nadir and sleep debt."""
        debt = max(0.0, float(sleep_debt_hours))
        hour = current_hour_24h % 24.0

        if debt >= 2.0:
            prescribed_duration = 30.0
            protocol_name = "Intensive Neurological Repair Protocol (30 min)"
        elif debt >= 1.0 or morning_cognitive_load.lower() == "high":
            prescribed_duration = 20.0
            protocol_name = "Circadian Postprandial Dip Counter-Strategy (20 min)"
        else:
            prescribed_duration = 10.0
            protocol_name = "Acute Cognitive Acuity & Dopamine Reset (10 min)"

        # Optimal circadian timing: typically between 13:00 and 16:00
        ideal_window = "13:30 - 15:30"
        is_in_optimal_window = 13.0 <= hour <= 16.0

        return {
            "sleep_debt_hours": debt,
            "morning_cognitive_load": morning_cognitive_load,
            "prescribed_protocol": protocol_name,
            "recommended_duration_minutes": prescribed_duration,
            "optimal_circadian_window_24h": ideal_window,
            "timing_alignment_status": "Optimal entrainment window" if is_in_optimal_window else "Acceptable off-peak reset",
            "execution_instructions": (
                "Lie supine in a darkened, temperature-neutral room. Utilize belly diaphragmatic breathing "
                "with prolonged exhalations (4s inhale, 8s exhale). Avoid cognitive visualization effort; allow peripheral sensory gating."
            )
        }
