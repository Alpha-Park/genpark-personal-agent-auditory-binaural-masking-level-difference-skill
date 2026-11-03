---
name: genpark-personal-agent-auditory-binaural-masking-level-difference-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for evaluating Auditory Binaural Masking Level Difference (BMLD), brainstem auditory pathways, and cocktail party speech-in-noise perception.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Auditory Binaural Masking Level Difference (BMLD) Skill

A sovereign personal agent capability for psychoacoustic modeling of central auditory processing, brainstem interaural phase encoding, and speech-in-noise cocktail party optimization.

## Core Capabilities
- **BMLD Metric Extraction**: Calculates homophasic ($S_0 N_0$) vs antiphasic ($S_\pi N_0$) threshold difference in decibels.
- **Brainstem Processing Score**: Evaluates superior olivary complex phase locking and central binaural squelch.
- **Cocktail Party Intelligibility**: Projects percentage improvement in speech discrimination against ambient background noise.
- **Personalized Ergonomic Recommendations**: Provides acoustic environment adaptations and audio device tuning.

## Fast Invocation
```python
from client import BinauralMaskingLevelDifferenceClient

client = BinauralMaskingLevelDifferenceClient()
res = client.evaluate_bmld(
    s0_n0_threshold_db=64.0,
    spi_n0_threshold_db=50.0,
    test_frequency_hz=500.0
)
print("BMLD:", res["bmld_db"], "dB")
print("Intelligibility Boost:", res["speech_in_noise_boost_pct"], "%")
```
