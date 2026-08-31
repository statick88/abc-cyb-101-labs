#!/usr/bin/env bash
set -euo pipefail
STUDENT="${1:-alumno-001}"
LAB_DIR="/home/kali/cybersec-lab/module-01"
FILE="${LAB_DIR}/CORE-MOD1-01-cia.md"
if [[ -f "$FILE" ]] && [[ -s "$FILE" ]]; then
  echo "PASSED: $FILE exists and has content"
  exit 0
else
  echo "FAILED: Missing or empty $FILE"
  exit 1
fi
