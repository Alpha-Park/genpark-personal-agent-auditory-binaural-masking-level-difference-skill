"""
Example Usage: Auditory Binaural Masking Level Difference (BMLD) Evaluation.
Demonstrates psychoacoustic release from masking and brainstem processing scoring.
"""

from client import BinauralMaskingLevelDifferenceClient


def main():
    client = BinauralMaskingLevelDifferenceClient()
    print("=== Auditory Binaural Masking Level Difference (BMLD) Demo ===")

    # Test Case 1: Intact brainstem binaural unmasking (Young healthy adult)
    res1 = client.evaluate_bmld(
        s0_n0_threshold_db=64.0,
        spi_n0_threshold_db=50.0,
        test_frequency_hz=500.0,
        sm_n0_threshold_db=62.0
    )
    print("\nTest Case 1: Healthy Auditory System (500 Hz)")
    print(f"  Homophasic S0N0: {res1['s0_n0_threshold_db']} dB | Antiphasic SpiN0: {res1['spi_n0_threshold_db']} dB")
    print(f"  BMLD: {res1['bmld_db']} dB")
    print(f"  Brainstem Processing Score: {res1['brainstem_processing_score']} / 100")
    print(f"  Cocktail Party Intelligibility Boost: +{res1['speech_in_noise_boost_pct']}%")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Borderline / mild deficit
    res2 = client.evaluate_bmld(
        s0_n0_threshold_db=60.0,
        spi_n0_threshold_db=53.5,
        test_frequency_hz=500.0
    )
    print("\nTest Case 2: Mild Deficit")
    print(f"  BMLD: {res2['bmld_db']} dB")
    print(f"  Brainstem Score: {res2['brainstem_processing_score']} / 100")
    print(f"  Classification: {res2['classification']}")

    # Test Case 3: Central auditory processing impairment / pontine lesion
    res3 = client.evaluate_bmld(
        s0_n0_threshold_db=62.0,
        spi_n0_threshold_db=59.5,
        test_frequency_hz=500.0
    )
    print("\nTest Case 3: Compromised Central Auditory Integration")
    print(f"  BMLD: {res3['bmld_db']} dB")
    print(f"  Brainstem Score: {res3['brainstem_processing_score']} / 100")
    print(f"  Classification: {res3['classification']}")
    print(f"  Guidance: {res3['actionable_guidance']}")


if __name__ == "__main__":
    main()
