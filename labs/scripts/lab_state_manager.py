#!/usr/bin/env python3
"""
lab_state_manager.py — Gestión de estado y firma de retos CORE
Ruta: /usr/local/lib/lab_state_manager.py
Uso: python3 lab_state_manager.py --student-id <id> --challenge-id <id> --status <PASSED|FAILED> [--timestamp <ISO>] [--export <file>]
"""

import argparse
import json
import os
import sys
import hashlib
import hmac
from datetime import datetime, timezone
from pathlib import Path

# Configuración
LAB_STATE_DIR = "/var/lab-state"
SECRET_FILE = os.path.join(LAB_STATE_DIR, ".secret")
INDEX_FILE = os.path.join(LAB_STATE_DIR, "index.json")

# Módulos y títulos para enriquecimiento de metadatos
MODULE_METADATA = {
    "1": "Principios de Ciberseguridad y Gestión de Riesgo",
    "2": "Seguridad en Redes y Controles Perimetrales",
    "3": "Hardening de Sistemas e Identidades",
    "4": "Amenazas, Criptografía y Gestión de Vulnerabilidades",
    "5": "Logging, SIEM, Respuesta a Incidentes y BCP/DRP",
}

CHALLENGE_TITLES = {
    "CORE-MOD1-01": "Identificar pilares CIA en incidente",
    "CORE-MOD1-02": "Calcular riesgo inherente y residual",
    "CORE-MOD1-03": "Clasificar activos por criticidad",
    "CORE-MOD1-04": "Mapear controles a funciones CSF 2.0",
    "CORE-MOD1-05": "Diseñar tratamiento de riesgo",
    "CORE-MOD1-06": "Elaborar informe de brechas NIST CSF",
    "CORE-MOD2-01": "Capturar tráfico HTTP no cifrado",
    "CORE-MOD2-02": "Detectar escaneo Nmap SYN",
    "CORE-MOD2-03": "Configurar regla UFW denegar RDP",
    "CORE-MOD2-04": "Configurar regla iptables permitir SSH",
    "CORE-MOD2-05": "Diseñar arquitectura DMZ 3 zonas",
    "CORE-MOD2-06": "Correlacionar IP con reputación",
    "CORE-MOD2-07": "Identificar protocolos en .pcapng",
    "CORE-MOD2-08": "Probar conectividad entre zonas",
    "CORE-MOD2-09": "Analizar alerta de IDS (TP/FP)",
    "CORE-MOD2-10": "Configurar logging de firewall",
    "CORE-MOD2-11": "Detectar consultas DNS anómalas",
    "CORE-MOD2-12": "Documentar arquitectura de defensa",
    "CORE-MOD3-01": "Deshabilitar servicio innecesario (Telnet)",
    "CORE-MOD3-02": "Configurar política de passwords",
    "CORE-MOD3-03": "Habilitar logging de eventos",
    "CORE-MOD3-04": "Aplicar actualizaciones automáticas",
    "CORE-MOD3-05": "Diseñar modelo RBAC 5 roles",
    "CORE-MOD3-06": "Configurar sudoers con privilegios mínimos",
    "CORE-MOD3-07": "Remover permiso SUID innecesario",
    "CORE-MOD3-08": "Configurar MFA TOTP",
    "CORE-MOD3-09": "Comparar factores de autenticación",
    "CORE-MOD3-10": "Diseñar política MFA para roles privilegiados",
    "CORE-MOD3-11": "Evaluar cumplimiento ISO 27001",
    "CORE-MOD3-12": "Documentar proceso de hardening",
    "CORE-MOD3-13": "Verificar cumplimiento CIS Benchmark",
    "CORE-MOD4-01": "Analizar correo de phishing (indicadores)",
    "CORE-MOD4-02": "Identificar familia de ransomware",
    "CORE-MOD4-03": "Cifrar archivo con AES-256-GCM",
    "CORE-MOD4-04": "Generar par RSA-2048",
    "CORE-MOD4-05": "Calcular hash SHA-256",
    "CORE-MOD4-06": "Calcular CVSS Base (RCE)",
    "CORE-MOD4-07": "Calcular CVSS Base (XSS)",
    "CORE-MOD4-08": "Interpretar métricas ambientales",
    "CORE-MOD4-09": "Analizar reporte Nessus Essentials",
    "CORE-MOD4-10": "Proponer plan de remediación priorizado",
    "CORE-MOD4-11": "Detectar vector de ataque en escenario",
    "CORE-MOD4-12": "Documentar persistencia de malware",
    "CORE-MOD4-13": "Integrar hallazgos en informe unificado",
    "CORE-MOD4-14": "Proponer controles correctivos y preventivos",
    "CORE-MOD5-01": "Analizar log de acceso (intentos fallidos)",
    "CORE-MOD5-02": "Detectar acceso en horario no habitual",
    "CORE-MOD5-03": "Correlacionar login con cambios de config",
    "CORE-MOD5-04": "Configurar regla de correlación (brute force)",
    "CORE-MOD5-05": "Crear playbook de ransomware (7+ pasos)",
    "CORE-MOD5-06": "Calcular métricas MTTD/MTTC/MTTR",
    "CORE-MOD5-07": "Diseñar tabla de escalación",
    "CORE-MOD5-08": "Diseñar plan de respaldos (RTO/RPO)",
    "CORE-MOD5-09": "Configurar Nginx reverse proxy (HTTP→HTTPS)",
    "CORE-MOD5-10": "Analizar access logs Nginx (patrones de ataque)",
    "CORE-MOD5-11": "Desplegar stack Docker Compose multi-servicio",
    "CORE-MOD5-12": "Validar conectividad entre servicios Docker",
    "CORE-MOD5-13": "Documentar playbook de incidente",
    "CORE-MOD5-14": "Integrar análisis de logs + TLS + Docker",
    "CORE-MOD5-15": "Presentar estrategia de respaldos en Markdown",
}


def ensure_dirs():
    """Crea directorios de estado si no existen."""
    os.makedirs(LAB_STATE_DIR, exist_ok=True)
    os.makedirs(os.path.join(LAB_STATE_DIR, "progress"), exist_ok=True)


def get_or_create_secret() -> bytes:
    """Obtiene o genera el secreto HMAC local."""
    if not os.path.exists(SECRET_FILE):
        secret = hashlib.sha256(os.urandom(64)).hexdigest()
        with open(SECRET_FILE, "w") as f:
            f.write(secret)
        os.chmod(SECRET_FILE, 0o600)
        return secret.encode()
    with open(SECRET_FILE, "r") as f:
        return f.read().strip().encode()


def compute_hmac(challenge_id: str, status: str, timestamp: str, secret: bytes) -> str:
    """Calcula HMAC-SHA256 para un registro de reto."""
    message = f"{challenge_id}|{status}|{timestamp}"
    return hmac.new(secret, message.encode(), hashlib.sha256).hexdigest()


def load_index(student_id: str) -> dict:
    """Carga el índice global del estudiante."""
    index_path = os.path.join(LAB_STATE_DIR, "progress", student_id, "index.json")
    if os.path.exists(index_path):
        with open(index_path, "r") as f:
            return json.load(f)
    return {
        "student_id": student_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "total_core": 60,
        "passed_core": 0,
        "failed_core": 0,
        "pending_core": 60,
        "challenges": [],
        "completed": [],
        "failed": [],
    }


def save_index(student_id: str, index: dict):
    """Persiste el índice global del estudiante."""
    index_path = os.path.join(LAB_STATE_DIR, "progress", student_id, "index.json")
    index["updated_at"] = datetime.now(timezone.utc).isoformat()
    with open(index_path, "w") as f:
        json.dump(index, f, indent=2)


def register_challenge(student_id: str, challenge_id: str, status: str, timestamp: str, secret: bytes):
    """Registra un reto completado/fallido con firma HMAC."""
    student_dir = os.path.join(LAB_STATE_DIR, "progress", student_id)
    os.makedirs(student_dir, exist_ok=True)

    # Enriquecer metadatos
    module = challenge_id.split("-")[1].replace("MOD", "")
    title = CHALLENGE_TITLES.get(challenge_id, challenge_id)

    record = {
        "student_id": student_id,
        "challenge_id": challenge_id,
        "module": int(module) if module.isdigit() else 0,
        "title": title,
        "status": status,
        "timestamp": timestamp,
        "hash_signature": f"sha256:{compute_hmac(challenge_id, status, timestamp, secret)}",
        "attempts": 1,
        "validator": "bash",
        "artifacts": [],
    }

    # Guardar registro individual
    record_path = os.path.join(student_dir, f"{challenge_id}.json")
    with open(record_path, "w") as f:
        json.dump(record, f, indent=2)

    # Actualizar índice
    index = load_index(student_id)
    if challenge_id not in index["challenges"]:
        index["challenges"].append(challenge_id)

    if status == "PASSED":
        if challenge_id not in index["completed"]:
            index["completed"].append(challenge_id)
        if challenge_id in index["failed"]:
            index["failed"].remove(challenge_id)
    elif status == "FAILED":
        if challenge_id not in index["failed"]:
            index["failed"].append(challenge_id)

    index["passed_core"] = len(index["completed"])
    index["failed_core"] = len(index["failed"])
    index["pending_core"] = index["total_core"] - index["passed_core"] - index["failed_core"]
    save_index(student_id, index)


def export_signature(student_id: str, export_file: str):
    """Exporta firma de progreso para entrega."""
    index = load_index(student_id)
    secret = get_or_create_secret()
    timestamp = datetime.now(timezone.utc).isoformat()

    # Calcular firma global del índice
    index_message = json.dumps(index, sort_keys=True)
    global_signature = hmac.new(secret, index_message.encode(), hashlib.sha256).hexdigest()

    export_content = f"""# Firma de Progreso — ABC-CYB-101
Estudiante: {student_id}
Fecha de exportación: {timestamp}
Firma global (HMAC-SHA256): sha256:{global_signature}

## Resumen
- Total retos CORE: {index['total_core']}
- Aprobados: {index['passed_core']}
- Reprobados: {index['failed_core']}
- Pendientes: {index['pending_core']}
- Progreso: {index['passed_core'] * 100 // index['total_core']}%

## Retos completados
{chr(10).join('- ' + c for c in index['completed'])}

## Retos reprobados
{chr(10).join('- ' + c for c in index['failed'])}

## Verificación
Este documento puede ser verificado contra el índice oficial del curso.
"""

    with open(export_file, "w") as f:
        f.write(export_content)

    print(f"Firma exportada a: {export_file}")


def main():
    parser = argparse.ArgumentParser(description="Gestión de estado de retos CORE")
    parser.add_argument("--student-id", required=True, help="ID del estudiante")
    parser.add_argument("--challenge-id", help="ID del reto (ej. CORE-MOD1-01)")
    parser.add_argument("--status", choices=["PASSED", "FAILED"], help="Estado del reto")
    parser.add_argument("--timestamp", help="Timestamp ISO 8601")
    parser.add_argument("--export", help="Archivo de exportación de firma")
    parser.add_argument("--state-dir", default=LAB_STATE_DIR, help="Directorio de estado")

    args = parser.parse_args()

    ensure_dirs()
    secret = get_or_create_secret()

    if args.export:
        export_signature(args.student_id, args.export)
        return 0

    if not args.challenge_id or not args.status:
        parser.error("--challenge-id y --status son requeridos para registrar un reto")

    timestamp = args.timestamp or datetime.now(timezone.utc).isoformat()
    register_challenge(args.student_id, args.challenge_id, args.status, timestamp, secret)

    print(f"Reto {args.challenge_id} registrado como {args.status} para {args.student_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
