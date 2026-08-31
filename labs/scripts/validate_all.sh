#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VALIDATORS_DIR="/opt/labs/validators"
STUDENT="${1:-alumno-001}"
PASSED=0
FAILED=0
TOTAL=0

echo "=== Validación de Retos CORE — ABC-CYB-101 ==="
echo "Estudiante: ${STUDENT}"
echo ""

for module in $(seq -w 1 5); do
  MODULE_DIR="${VALIDATORS_DIR}/module-${module}"
  if [[ ! -d "$MODULE_DIR" ]]; then
    continue
  fi
  echo "--- Módulo ${module} ---"
  for validator in "${MODULE_DIR}"/validate-*.sh; do
    [[ -x "$validator" ]] || continue
    CHALLENGE=$(basename "$validator" .sh | sed 's/validate-//')
    TOTAL=$((TOTAL + 1))
    if "$validator" "$STUDENT"; then
      PASSED=$((PASSED + 1))
    else
      FAILED=$((FAILED + 1))
    fi
  done
done

echo ""
echo "=== Resumen ==="
echo "Total: ${TOTAL} | Aprobados: ${PASSED} | Reprobados: ${FAILED}"
echo "Progreso: ${PASSED} / ${TOTAL} ($(awk "BEGIN {printf \"%.1f\", (${PASSED}/${TOTAL})*100}")%)"

if [[ $FAILED -gt 0 ]]; then
  exit 1
fi
exit 0
