"""
MCP Server for Auditory Binaural Masking Level Difference (BMLD) Skill.
Exposes JSON-RPC Model Context Protocol tools for psychoacoustic masking release and central auditory evaluation.
"""

import sys
import json
from typing import Dict, Any
from client import BinauralMaskingLevelDifferenceClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_bmld",
                "description": "Calculates Binaural Masking Level Difference (BMLD in dB), brainstem processing score, and cocktail party speech-in-noise intelligibility boost.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "s0_n0_threshold_db": {
                            "type": "number",
                            "description": "Homophasic masked hearing threshold in dB SPL/HL (signal and noise in phase, e.g. 62.0)."
                        },
                        "spi_n0_threshold_db": {
                            "type": "number",
                            "description": "Antiphasic masked hearing threshold in dB SPL/HL (signal 180 deg out of phase, e.g. 48.0)."
                        },
                        "test_frequency_hz": {
                            "type": "number",
                            "description": "Acoustic test frequency in Hz (typically 500.0 or 250.0 Hz).",
                            "default": 500.0
                        },
                        "sm_n0_threshold_db": {
                            "type": "number",
                            "description": "Optional monaural signal masked threshold in dB."
                        }
                    },
                    "required": ["s0_n0_threshold_db", "spi_n0_threshold_db"]
                }
            }
        ]
    }


def handle_request(client: BinauralMaskingLevelDifferenceClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_bmld":
            sm_val = args.get("sm_n0_threshold_db")
            if sm_val is not None:
                sm_val = float(sm_val)

            res = client.evaluate_bmld(
                s0_n0_threshold_db=float(args.get("s0_n0_threshold_db", 62.0)),
                spi_n0_threshold_db=float(args.get("spi_n0_threshold_db", 48.0)),
                test_frequency_hz=float(args.get("test_frequency_hz", 500.0)),
                sm_n0_threshold_db=sm_val
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = BinauralMaskingLevelDifferenceClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
