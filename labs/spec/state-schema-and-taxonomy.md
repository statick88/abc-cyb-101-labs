# Especificación de Estado y Taxonomía de Retos — ABC-CYB-101

## 1. Esquema de Persistencia `/var/lab-state/progress`

### 1.1 Formato JSON por reto

Cada reto completado genera un registro en:

/var/lab-state/progress/<student_id>/<challenge_id>.json

```json
{
  "student_id": "alumno-001",
  "challenge_id": "CORE-MOD1-01",
  "module": 1,
  "title": "Identificar pilares CIA en incidente",
  "status": "PASSED",
  "timestamp": "2026-08-31T19:45:00Z",
  "hash_signature": "sha256:<hmac_hex>",
  "attempts": 2,
  "validator": "bash",
  "artifacts": [
    "/home/kali/cybersec-lab/module-01/reporte-cia.md"
  ]
}
```

### 1.2 Esquema de índice global

/var/lab-state/progress/index.json

```json
{
  "student_id": "alumno-001",
  "created_at": "2026-08-31T19:00:00Z",
  "updated_at": "2026-08-31T19:45:00Z",
  "total_core": 60,
  "passed_core": 0,
  "failed_core": 0,
  "pending_core": 60,
  "challenges": [
    "CORE-MOD1-01",
    "CORE-MOD1-02"
  ],
  "completed": [],
  "failed": []
}
```

### 1.3 Política de firma

- Se usa HMAC-SHA256 con secreto local `/var/lab-state/.secret`.
- El validador calcula: `echo -n "${challenge_id}|${status}|${timestamp}" | sha256hmac`.
- Cualquier modificación externa del JSON invalida la firma.

## 2. Taxonomía de los 60 Retos CORE

### Módulo I — 6 Retos CORE

| ID | Título | Ámbito |
|----|--------|--------|
| CORE-MOD1-01 | Identificar pilares CIA en incidente | ISO 27001 / NIST CSF 2.0 |
| CORE-MOD1-02 | Calcular riesgo inherente y residual | ISO 31000 / NIST SP 800-30 |
| CORE-MOD1-03 | Clasificar activos por criticidad | Gobierno / Identificar |
| CORE-MOD1-04 | Mapear controles a funciones CSF 2.0 | Proteger / Detectar / Responder / Recuperar |
| CORE-MOD1-05 | Diseñar tratamiento de riesgo | Aceptar / Mitigar / Transferir / Evitar |
| CORE-MOD1-06 | Elaborar informe de brechas NIST CSF | Gobernar / Identificar |

### Módulo II — 12 Retos CORE

| ID | Título | Ámbito |
|----|--------|--------|
| CORE-MOD2-01 | Capturar tráfico HTTP no cifrado | Wireshark / TCP-IP |
| CORE-MOD2-02 | Detectar escaneo Nmap SYN | IDS / Suricata |
| CORE-MOD2-03 | Configurar regla UFW denegar RDP | Firewall / UFW |
| CORE-MOD2-04 | Configurar regla iptables permitir SSH | Firewall / iptables |
| CORE-MOD2-05 | Diseñar arquitectura DMZ 3 zonas | Defensa perimetral |
| CORE-MOD2-06 | Correlacionar IP con reputación | Análisis de tráfico |
| CORE-MOD2-07 | Identificar protocolos en .pcapng | Wireshark |
| CORE-MOD2-08 | Probar conectividad entre zonas | Segmentación |
| CORE-MOD2-09 | Analizar alerta de IDS (TP/FP) | Suricata / Snort |
| CORE-MOD2-10 | Configurar logging de firewall | iptables / UFW logging |
| CORE-MOD2-11 | Detectar consultas DNS anómalas | DNS / longitud subdominio |
| CORE-MOD2-12 | Documentar arquitectura de defensa | Informe perimetral |

### Módulo III — 13 Retos CORE

| ID | Título | Ámbito |
|----|--------|--------|
| CORE-MOD3-01 | Deshabilitar servicio innecesario (Telnet) | Hardening CIS |
| CORE-MOD3-02 | Configurar política de passwords | Hardening / PAM |
| CORE-MOD3-03 | Habilitar logging de eventos | auditd / rsyslog |
| CORE-MOD3-04 | Aplicar actualizaciones automáticas | Hardening |
| CORE-MOD3-05 | Diseñar modelo RBAC 5 roles | IAM / RBAC |
| CORE-MOD3-06 | Configurar sudoers con privilegios mínimos | SUID / sudoers |
| CORE-MOD3-07 | Remover permiso SUID innecesario | SUID / find / permissions |
| CORE-MOD3-08 | Configurar MFA TOTP | MFA / Google Authenticator |
| CORE-MOD3-09 | Comparar factores de autenticación | MFA phishing-resistant |
| CORE-MOD3-10 | Diseñar política MFA para roles privilegiados | MFA / políticas |
| CORE-MOD3-11 | Evaluar cumplimiento ISO 27001 | Auditoría / ISO 27001 |
| CORE-MOD3-12 | Documentar proceso de hardening | Informe hardening |
| CORE-MOD3-13 | Verificar cumplimiento CIS Benchmark | CIS / scripts |

### Módulo IV — 14 Retos CORE

| ID | Título | Ámbito |
|----|--------|--------|
| CORE-MOD4-01 | Analizar correo de phishing (indicadores) | Ingeniería social |
| CORE-MOD4-02 | Identificar familia de ransomware | Malware / análisis |
| CORE-MOD4-03 | Cifrar archivo con AES-256-GCM | OpenSSL / simétrico |
| CORE-MOD4-04 | Generar par RSA-2048 | OpenSSL / asimétrico |
| CORE-MOD4-05 | Calcular hash SHA-256 | OpenSSL / hashing |
| CORE-MOD4-06 | Calcular CVSS Base (RCE) | CVSS v3.1 |
| CORE-MOD4-07 | Calcular CVSS Base (XSS) | CVSS v3.1 |
| CORE-MOD4-08 | Interpretar métricas ambientales | CVSS ambiental |
| CORE-MOD4-09 | Analizar reporte Nessus Essentials | Vulnerabilidades |
| CORE-MOD4-10 | Proponer plan de remediación priorizado | Gestión de parches |
| CORE-MOD4-11 | Detectar vector de ataque en escenario | Superficie de ataque |
| CORE-MOD4-12 | Documentar persistencia de malware | Análisis de malware |
| CORE-MOD4-13 | Integrar hallazgos en informe unificado | Informe integrador |
| CORE-MOD4-14 | Proponer controles correctivos y preventivos | Defensa en profundidad |

### Módulo V — 15 Retos CORE

| ID | Título | Ámbito |
|----|--------|--------|
| CORE-MOD5-01 | Analizar log de acceso (intentos fallidos) | Logging |
| CORE-MOD5-02 | Detectar acceso en horario no habitual | Logging / UEBA |
| CORE-MOD5-03 | Correlacionar login con cambios de config | SIEM / correlación |
| CORE-MOD5-04 | Configurar regla de correlación (brute force) | SIEM / Splunk |
| CORE-MOD5-05 | Crear playbook de ransomware (7+ pasos) | IR / NIST SP 800-61 |
| CORE-MOD5-06 | Calcular métricas MTTD/MTTC/MTTR | IR / métricas |
| CORE-MOD5-07 | Diseñar tabla de escalación | IR / comunicación |
| CORE-MOD5-08 | Diseñar plan de respaldos (RTO/RPO) | BCP / DRP |
| CORE-MOD5-09 | Configurar Nginx reverse proxy (HTTP→HTTPS) | Nginx / TLS |
| CORE-MOD5-10 | Analizar access logs Nginx (patrones de ataque) | Nginx / logs |
| CORE-MOD5-11 | Desplegar stack Docker Compose multi-servicio | Docker / orquestación |
| CORE-MOD5-12 | Validar conectividad entre servicios Docker | Docker / redes |
| CORE-MOD5-13 | Documentar playbook de incidente | IR / documentación |
| CORE-MOD5-14 | Integrar análisis de logs + TLS + Docker | Proyecto integrador |
| CORE-MOD5-15 | Presentar estrategia de respaldos en Markdown | BCP / DRP / informe |

## 3. Matriz de Módulo → Reto → Validador

| Módulo | Retos CORE | Script Validador |
|--------|------------|------------------|
| Módulo I | 6 | labs/scripts/validators/module-01/ |
| Módulo II | 12 | labs/scripts/validators/module-02/ |
| Módulo III | 13 | labs/scripts/validators/module-03/ |
| Módulo IV | 14 | labs/scripts/validators/module-04/ |
| Módulo V | 15 | labs/scripts/validators/module-05/ |
