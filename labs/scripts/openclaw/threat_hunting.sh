#!/bin/bash
# threat_hunting.sh
# Hypothesis-Based Threat Hunting para Agentes IA
# Nivel: Medio-Alto

echo "=== Threat Hunting - Agentes IA ==="
echo ""

cat << 'EOF'
# Hipotesis de Investigacion

## H1: Credenciales comprometidas
- **Indicators**: Multiples IPs originando, horarios inusuales
- **Tools**: Log analysis, SIEM queries
- **Hunting**: Buscar creds en dark web

## H2: Prompt Injection activo
- **Indicators**: Tokens extraeos, respuestas anmalas
- **Hunting**: Analyze conversation logs
- **Hunting**: Input/output correlation

## H3: Modelo comprometido
- **Indicators**: Respuestas fuera de contexto, cambios de comportamiento
- **Hunting**: Conversation baseline analysis
- **Hunting**: Fine-tuning detection

## H4: Sandbox escape
- **Indicators**: File descriptors extraeos, environment manipulation
- **Hunting**: System call monitoring
- **Hunting**: Container escape indicators
EOF

echo ""
echo "=== Instrucciones ==="
echo "1. Selecciona una hipotesis (H1-H4)"
echo "2. Ejecuta las queries de SIEM correspondientes"
echo "3. Documenta hallazgos en el reporte de hunting"
