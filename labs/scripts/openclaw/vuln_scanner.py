#!/usr/bin/env python3
"""
Advanced OpenClaw Vulnerability Scanner
Nivel: Medio-Alto
"""

import json
import socket
import sys

try:
    import colorama
    from colorama import Fore, Style
    colorama.init()
except ImportError:
    # Fallback sin colores
    class _Fore:
        CYAN = GREEN = YELLOW = RED = ""
    class _Style:
        RESET_ALL = ""
    Fore, Style = _Fore(), _Style()


class OpenClawVulnScanner:
    def __init__(self, target: str):
        self.target = target
        self.findings: list[dict] = []
        self.ports = {
            8080: "OpenClaw HTTP",
            8443: "OpenClaw HTTPS",
            9390: "OpenVAS",
            9391: "OpenVAS Greenbone",
        }

    def scan_ports(self) -> list[dict]:
        """Escanear puertos comunes de OpenClaw."""
        print(f"{Fore.CYAN}[*] Escaneando puertos en {self.target}...{Style.RESET_ALL}")
        for port, service in self.ports.items():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((self.target, port))
                sock.close()
                if result == 0:
                    print(f"{Fore.GREEN}[+] {service} encontrado en puerto {port}{Style.RESET_ALL}")
                    self.findings.append({"port": port, "service": service, "status": "open"})
            except Exception:
                pass
        return self.findings

    def check_cve_41371(self) -> list[dict]:
        """Verificar presencia de CVE-2026-41371."""
        print(f"{Fore.CYAN}[*] Verificando CVE-2026-41371...{Style.RESET_ALL}")
        ws_url = f"ws://{self.target}:8080/ws"
        print(f"  [-] WebSocket endpoint: {ws_url}")
        print(f"  [!] Requiere verificacion manual con cve_41371.py")
        self.findings.append({"cve": "CVE-2026-41371", "status": "untested"})
        return self.findings

    def check_config_issues(self) -> list[dict]:
        """Verificar configuraciones inseguras comunes."""
        print(f"{Fore.CYAN}[*] Verificando configuraciones...{Style.RESET_ALL}")
        issues = [
            ("API key expuesta?", "Revisar variables de entorno"),
            ("Running as root?", "Verificar usuario del proceso"),
            ("CORS enabled?", "Verificar headers HTTP"),
            ("WebSocket sin WSS?", "Verificar TLS activado"),
        ]
        for issue, desc in issues:
            print(f"  [!] {issue}: {desc}")
            self.findings.append({"config": issue, "description": desc})
        return self.findings

    def generate_report(self) -> dict:
        """Generar reporte JSON de vulnerabilidades."""
        report = {"target": self.target, "findings": self.findings}
        print(f"\n{Fore.YELLOW}=== REPORTE DE VULNERABILIDADES ==={Style.RESET_ALL}")
        print(json.dumps(report, indent=2))
        return report


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 vuln_scanner.py <target_ip>")
        sys.exit(1)

    target = sys.argv[1]
    scanner = OpenClawVulnScanner(target)

    print(f"{Fore.CYAN}=== OpenClaw Vulnerability Scanner ==={Style.RESET_ALL}")
    print(f"Target: {target}\n")

    scanner.scan_ports()
    print()
    scanner.check_cve_41371()
    print()
    scanner.check_config_issues()
    print()
    scanner.generate_report()


if __name__ == "__main__":
    main()
