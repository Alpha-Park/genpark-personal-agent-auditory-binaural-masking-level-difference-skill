# Auditory Binaural Masking Level Difference (BMLD) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive psychoacoustic modeling of Binaural Masking Level Difference (BMLD), brainstem auditory squelch, and cocktail party speech-in-noise intelligibility.

```mermaid
flowchart TD
    Dichotic["Dichotic Hearing Test (S0N0 vs SpiN0)"] --> Phase["Interaural Phase Difference (IPD) Extraction"]
    Phase --> BMLD_Calc["BMLD dB Decibel Advantage Engine"]
    BMLD_Calc --> Brainstem["Brainstem Processing & Speech Intelligibility Scoring"]
    Brainstem --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Audiological Standard Formulas**: Implements clinically validated homophasic and antiphasic decibel differential modeling.
- **Cocktail Party Intelligibility Modeling**: Direct calculation of speech perception advantage in background noise.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import BinauralMaskingLevelDifferenceClient

client = BinauralMaskingLevelDifferenceClient()
result = client.evaluate_bmld(
    s0_n0_threshold_db=64.0,
    spi_n0_threshold_db=50.0,
    test_frequency_hz=500.0
)
print("BMLD:", result["bmld_db"], "dB")
print("Brainstem Score:", result["brainstem_processing_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
