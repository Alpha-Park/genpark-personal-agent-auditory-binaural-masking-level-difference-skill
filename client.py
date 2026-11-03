"""
Auditory Binaural Masking Level Difference (BMLD) & Central Auditory Processing Engine.
Provides deterministic, zero-dependency psychoacoustic modeling of homophasic (S0N0) vs
antiphasic (SpiN0) thresholds, binaural squelch, and brainstem auditory processing efficiency.
"""

from typing import Dict, Any, List, Optional


class BinauralMaskingLevelDifferenceClient:
    """
    Deterministic client for evaluating Auditory Binaural Masking Level Difference (BMLD).
    Standard audiological psychoacoustic metric evaluating brainstem (superior olivary complex)
    binaural unmasking and speech-in-noise cocktail party performance.
    """

    def __init__(self):
        pass

    def evaluate_bmld(
        self,
        s0_n0_threshold_db: float,
        spi_n0_threshold_db: float,
        test_frequency_hz: float = 500.0,
        sm_n0_threshold_db: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Calculates BMLD = S0N0 threshold - SpiN0 threshold (in dB).
        Normal healthy adults at 500 Hz exhibit a BMLD release of 10.0 to 15.0 dB.
        """
        if test_frequency_hz <= 0:
            return {"error": "Test frequency must be positive"}

        bmld_db = round(s0_n0_threshold_db - spi_n0_threshold_db, 1)

        # Monaural unmasking if provided
        monaural_advantage_db = None
        if sm_n0_threshold_db is not None:
            monaural_advantage_db = round(sm_n0_threshold_db - spi_n0_threshold_db, 1)

        # Brainstem Binaural Processing Score (0 - 100):
        # Target BMLD >= 12.0 dB -> 90 - 100.
        # BMLD 8.0 - 11.9 dB -> 70 - 89.
        # BMLD < 7.0 dB -> < 60 (Central auditory processing attenuation).
        if bmld_db >= 13.0:
            score = min(100.0, 92.0 + (bmld_db - 13.0) * 2.5)
        elif bmld_db >= 10.0:
            score = 80.0 + ((bmld_db - 10.0) / 3.0) * 12.0
        elif bmld_db >= 7.0:
            score = 60.0 + ((bmld_db - 7.0) / 3.0) * 19.0
        elif bmld_db >= 4.0:
            score = 35.0 + ((bmld_db - 4.0) / 3.0) * 24.0
        else:
            score = max(5.0, 35.0 - (4.0 - bmld_db) * 8.0)

        brainstem_score = round(min(100.0, max(5.0, score)), 1)

        # Speech-in-Noise cocktail party intelligibility enhancement prediction (dB SNR equivalent)
        # Each dB of BMLD equates to approximately 8-10% improvement in word recognition in noise.
        intelligibility_boost_pct = round(min(100.0, max(0.0, bmld_db * 7.5)), 1)

        if bmld_db >= 11.0:
            tier = "ROBUST_BINAURAL_UNMASKING"
            interp = f"Exceptional binaural squelch and interaural time difference (ITD) resolution (BMLD {bmld_db} dB at {test_frequency_hz} Hz)."
            guidance = "Superior central auditory processing; high resistance to acoustic masking and noise fatigue in open-office environments."
        elif bmld_db >= 7.5:
            tier = "NORMAL_CENTRAL_AUDITORY_PROCESSING"
            interp = f"Preserved binaural phase sensitivity (BMLD {bmld_db} dB at {test_frequency_hz} Hz); intact brainstem auditory pathways."
            guidance = "Normal speech discrimination in multi-talker cocktail party environments."
        elif bmld_db >= 4.5:
            tier = "MILD_BINAURAL_INTEGRATION_DEFICIT"
            interp = f"Suboptimal binaural masking release (BMLD {bmld_db} dB); reduced interaural phase disparity encoding."
            guidance = "Recommend directional acoustic microphones, active noise cancellation, and auditory fatigue monitoring."
        else:
            tier = "COMPROMISED_CENTRAL_BINAURAL_PROCESSING"
            interp = f"Severely attenuated BMLD ({bmld_db} dB); indicates pontine / brainstem central auditory processing impairment."
            guidance = "Significantly degraded speech intelligibility in background noise. Suggest comprehensive diagnostic audiology and auditory evoked potential testing."

        return {
            "test_frequency_hz": test_frequency_hz,
            "s0_n0_threshold_db": s0_n0_threshold_db,
            "spi_n0_threshold_db": spi_n0_threshold_db,
            "bmld_db": bmld_db,
            "monaural_advantage_db": monaural_advantage_db,
            "brainstem_processing_score": brainstem_score,
            "speech_in_noise_boost_pct": intelligibility_boost_pct,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
