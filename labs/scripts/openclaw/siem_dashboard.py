#!/usr/bin/env python3
"""
Dashboard de monitoreo para agentes IA
Muestra logs y alertas de seguridad
"""

import sys
from datetime import datetime


class AgentDashboard:
    def __init__(self):
        self.alerts: list[dict] = []

    def add_alert(self, level: str, message: str, source: str):
        """Agregar alerta al dashboard."""
        self.alerts.append({
            "timestamp": datetime.now().isoformat(),
            "level": level,
            "message": message,
            "source": source,
        })

    def display(self):
        """Mostrar dashboard de alertas."""
        print("=" * 60)
        print("AGENT SECURITY DASHBOARD")
        print("=" * 60)
        print(f"Total alertas: {len(self.alerts)}\n")

        critical = sum(1 for a in self.alerts if a["level"] == "CRITICAL")
        high = sum(1 for a in self.alerts if a["level"] == "HIGH")
        medium = sum(1 for a in self.alerts if a["level"] == "MEDIUM")

        print(f"CRITICAL: {critical}")
        print(f"HIGH:     {high}")
        print(f"MEDIUM:   {medium}\n")

        print("Ultimas alertas:")
        for alert in self.alerts[-5:]:
            print(f"  [{alert['level']}] {alert['message']}")
            print(f"    {alert['timestamp']} - {alert['source']}")


if __name__ == "__main__":
    dashboard = AgentDashboard()
    dashboard.add_alert("CRITICAL", "CVE-2026-41371 attempt detected", "10.0.0.50")
    dashboard.add_alert("HIGH", "Failed login attempts", "10.0.0.51")
    dashboard.add_alert("MEDIUM", "Rate limit exceeded", "10.0.0.52")
    dashboard.display()
