# Matriz de Mapeo de Retos — ABC-CYB-101

## Propósito
Esta matriz mapea cada reto CORE a su comando de verificación, validador automático y archivo de entrega esperado.

## Estructura de directorios
```
labs/scripts/validators/
├── module-01/
│   └── validate-CORE-MOD1-01.sh … validate-CORE-MOD1-06.sh
├── module-02/
│   └── validate-CORE-MOD2-01.sh … validate-CORE-MOD2-12.sh
├── module-03/
│   └── validate-CORE-MOD3-01.sh … validate-CORE-MOD3-13.sh
├── module-04/
│   └── validate-CORE-MOD4-01.sh … validate-CORE-MOD4-14.sh
└── module-05/
    └── validate-CORE-MOD5-01.sh … validate-CORE-MOD5-15.sh
```

## Módulo I — Principios de Ciberseguridad y Gestión de Riesgo

| ID | Título | Archivo de entrega | Validador |
|----|--------|-------------------|-----------|
| CORE-MOD1-01 | Identificar pilares CIA en incidente | `module-01/CORE-MOD1-01-cia.md` | `validate-CORE-MOD1-01.sh` |
| CORE-MOD1-02 | Calcular riesgo inherente y residual | `module-01/CORE-MOD1-02-riesgo.md` | `validate-CORE-MOD1-02.sh` |
| CORE-MOD1-03 | Clasificar activos por criticidad | `module-01/CORE-MOD1-03-activos.md` | `validate-CORE-MOD1-03.sh` |
| CORE-MOD1-04 | Mapear controles a funciones CSF 2.0 | `module-01/CORE-MOD1-04-csf.md` | `validate-CORE-MOD1-04.sh` |
| CORE-MOD1-05 | Diseñar tratamiento de riesgo | `module-01/CORE-MOD1-05-tratamiento.md` | `validate-CORE-MOD1-05.sh` |
| CORE-MOD1-06 | Elaborar informe de brechas NIST CSF | `module-01/CORE-MOD1-06-informe.md` | `validate-CORE-MOD1-06.sh` |

## Módulo II — Seguridad en Redes y Controles Perimetrales

| ID | Título | Archivo de entrega | Validador |
|----|--------|-------------------|-----------|
| CORE-MOD2-01 | Capturar tráfico HTTP no cifrado | `module-02/CORE-MOD2-01-http.md` | `validate-CORE-MOD2-01.sh` |
| CORE-MOD2-02 | Detectar escaneo Nmap SYN | `module-02/CORE-MOD2-02-nmap.md` | `validate-CORE-MOD2-02.sh` |
| CORE-MOD2-03 | Configurar regla UFW denegar RDP | `module-02/CORE-MOD2-03-ufw.md` | `validate-CORE-MOD2-03.sh` |
| CORE-MOD2-04 | Configurar regla iptables permitir SSH | `module-02/CORE-MOD2-04-iptables.md` | `validate-CORE-MOD2-04.sh` |
| CORE-MOD2-05 | Diseñar arquitectura DMZ 3 zonas | `module-02/CORE-MOD2-05-dmz.md` | `validate-CORE-MOD2-05.sh` |
| CORE-MOD2-06 | Correlacionar IP con reputación | `module-02/CORE-MOD2-06-ip.md` | `validate-CORE-MOD2-06.sh` |
| CORE-MOD2-07 | Identificar protocolos en .pcapng | `module-02/CORE-MOD2-07-pcapng.md` | `validate-CORE-MOD2-07.sh` |
| CORE-MOD2-08 | Probar conectividad entre zonas | `module-02/CORE-MOD2-08-conectividad.md` | `validate-CORE-MOD2-08.sh` |
| CORE-MOD2-09 | Analizar alerta de IDS (TP/FP) | `module-02/CORE-MOD2-09-ids.md` | `validate-CORE-MOD2-09.sh` |
| CORE-MOD2-10 | Configurar logging de firewall | `module-02/CORE-MOD2-10-logging.md` | `validate-CORE-MOD2-10.sh` |
| CORE-MOD2-11 | Detectar consultas DNS anómalas | `module-02/CORE-MOD2-11-dns.md` | `validate-CORE-MOD2-11.sh` |
| CORE-MOD2-12 | Documentar arquitectura de defensa | `module-02/CORE-MOD2-12-arquitectura.md` | `validate-CORE-MOD2-12.sh` |

## Módulo III — Hardening de Sistemas e Identidades

| ID | Título | Archivo de entrega | Validador |
|----|--------|-------------------|-----------|
| CORE-MOD3-01 | Deshabilitar servicio innecesario (Telnet) | `module-03/CORE-MOD3-01-telnet.md` | `validate-CORE-MOD3-01.sh` |
| CORE-MOD3-02 | Configurar política de passwords | `module-03/CORE-MOD3-02-passwords.md` | `validate-CORE-MOD3-02.sh` |
| CORE-MOD3-03 | Habilitar logging de eventos | `module-03/CORE-MOD3-03-logging.md` | `validate-CORE-MOD3-03.sh` |
| CORE-MOD3-04 | Aplicar actualizaciones automáticas | `module-03/CORE-MOD3-04-updates.md` | `validate-CORE-MOD3-04.sh` |
| CORE-MOD3-05 | Diseñar modelo RBAC 5 roles | `module-03/CORE-MOD3-05-rbac.md` | `validate-CORE-MOD3-05.sh` |
| CORE-MOD3-06 | Configurar sudoers con privilegios mínimos | `module-03/CORE-MOD3-06-sudoers.md` | `validate-CORE-MOD3-06.sh` |
| CORE-MOD3-07 | Remover permiso SUID innecesario | `module-03/CORE-MOD3-07-suid.md` | `validate-CORE-MOD3-07.sh` |
| CORE-MOD3-08 | Configurar MFA TOTP | `module-03/CORE-MOD3-08-mfa.md` | `validate-CORE-MOD3-08.sh` |
| CORE-MOD3-09 | Comparar factores de autenticación | `module-03/CORE-MOD3-09-factores.md` | `validate-CORE-MOD3-09.sh` |
| CORE-MOD3-10 | Diseñar política MFA para roles privilegiados | `module-03/CORE-MOD3-10-politica-mfa.md` | `validate-CORE-MOD3-10.sh` |
| CORE-MOD3-11 | Evaluar cumplimiento ISO 27001 | `module-03/CORE-MOD3-11-iso27001.md` | `validate-CORE-MOD3-11.sh` |
| CORE-MOD3-12 | Documentar proceso de hardening | `module-03/CORE-MOD3-12-hardening.md` | `validate-CORE-MOD3-12.sh` |
| CORE-MOD3-13 | Verificar cumplimiento CIS Benchmark | `module-03/CORE-MOD3-13-cis.md` | `validate-CORE-MOD3-13.sh` |

## Módulo IV — Amenazas, Criptografía y Gestión de Vulnerabilidades

| ID | Título | Archivo de entrega | Validador |
|----|--------|-------------------|-----------|
| CORE-MOD4-01 | Analizar correo de phishing (indicadores) | `module-04/CORE-MOD4-01-phishing.md` | `validate-CORE-MOD4-01.sh` |
| CORE-MOD4-02 | Identificar familia de ransomware | `module-04/CORE-MOD4-02-ransomware.md` | `validate-CORE-MOD4-02.sh` |
| CORE-MOD4-03 | Cifrar archivo con AES-256-GCM | `module-04/CORE-MOD4-03-aes.md` | `validate-CORE-MOD4-03.sh` |
| CORE-MOD4-04 | Generar par RSA-2048 | `module-04/CORE-MOD4-04-rsa.md` | `validate-CORE-MOD4-04.sh` |
| CORE-MOD4-05 | Calcular hash SHA-256 | `module-04/CORE-MOD4-05-sha256.md` | `validate-CORE-MOD4-05.sh` |
| CORE-MOD4-06 | Calcular CVSS Base (RCE) | `module-04/CORE-MOD4-06-cvss-rce.md` | `validate-CORE-MOD4-06.sh` |
| CORE-MOD4-07 | Calcular CVSS Base (XSS) | `module-04/CORE-MOD4-07-cvss-xss.md` | `validate-CORE-MOD4-07.sh` |
| CORE-MOD4-08 | Interpretar métricas ambientales | `module-04/CORE-MOD4-08-ambientales.md` | `validate-CORE-MOD4-08.sh` |
| CORE-MOD4-09 | Analizar reporte Nessus Essentials | `module-04/CORE-MOD4-01-nessus.md` | `validate-CORE-MOD4-09.sh` |
| CORE-MOD4-10 | Proponer plan de remediación priorizado | `module-04/CORE-MOD4-10-remediacion.md` | `validate-CORE-MOD4-10.sh` |
| CORE-MOD4-11 | Detectar vector de ataque en escenario | `module-04/CORE-MOD4-11-vector.md` | `validate-CORE-MOD4-11.sh` |
| CORE-MOD4-12 | Documentar persistencia de malware | `module-04/CORE-MOD4-12-persistencia.md` | `validate-CORE-MOD4-12.sh` |
| CORE-MOD4-13 | Integrar hallazgos en informe unificado | `module-04/CORE-MOD4-13-informe.md` | `validate-CORE-MOD4-13.sh` |
| CORE-MOD4-14 | Proponer controles correctivos y preventivos | `module-04/CORE-MOD4-14-controles.md` | `validate-CORE-MOD4-14.sh` |

## Módulo V — Logging, SIEM, Respuesta a Incidentes y BCP/DRP

| ID | Título | Archivo de entrega | Validador |
|----|--------|-------------------|-----------|
| CORE-MOD5-01 | Analizar log de acceso (intentos fallidos) | `module-05/CORE-MOD5-01-log-acceso.md` | `validate-CORE-MOD5-01.sh` |
| CORE-MOD5-02 | Detectar acceso en horario no habitual | `module-05/CORE-MOD5-02-horario.md` | `validate-CORE-MOD5-02.sh` |
| CORE-MOD5-03 | Correlacionar login con cambios de config | `module-05/CORE-MOD5-03-correlacion.md` | `validate-CORE-MOD5-03.sh` |
| CORE-MOD5-04 | Configurar regla de correlación (brute force) | `module-05/CORE-MOD5-04-regla.md` | `validate-CORE-MOD5-04.sh` |
| CORE-MOD5-05 | Crear playbook de ransomware (7+ pasos) | `module-05/CORE-MOD5-05-playbook.md` | `validate-CORE-MOD5-05.sh` |
| CORE-MOD5-06 | Calcular métricas MTTD/MTTC/MTTR | `module-05/CORE-MOD5-06-metricas.md` | `validate-CORE-MOD5-06.sh` |
| CORE-MOD5-07 | Diseñar tabla de escalación | `module-05/CORE-MOD5-07-escalacion.md` | `validate-CORE-MOD5-07.sh` |
| CORE-MOD5-08 | Diseñar plan de respaldos (RTO/RPO) | `module-05/CORE-MOD5-08-respaldos.md` | `validate-CORE-MOD5-08.sh` |
| CORE-MOD5-09 | Configurar Nginx reverse proxy (HTTP→HTTPS) | `module-05/CORE-MOD5-09-nginx.md` | `validate-CORE-MOD5-09.sh` |
| CORE-MOD5-10 | Analizar access logs Nginx (patrones de ataque) | `module-05/CORE-MOD5-10-logs.md` | `validate-CORE-MOD5-10.sh` |
| CORE-MOD5-11 | Desplegar stack Docker Compose multi-servicio | `module-05/CORE-MOD5-11-docker.md` | `validate-CORE-MOD5-11.sh` |
| CORE-MOD5-12 | Validar conectividad entre servicios Docker | `module-05/CORE-MOD5-12-conectividad.md` | `validate-CORE-MOD5-12.sh` |
| CORE-MOD5-13 | Documentar playbook de incidente | `module-05/CORE-MOD5-13-playbook.md` | `validate-CORE-MOD5-13.sh` |
| CORE-MOD5-14 | Integrar análisis de logs + TLS + Docker | `module-05/CORE-MOD5-14-integrador.md` | `validate-CORE-MOD5-14.sh` |
| CORE-MOD5-15 | Presentar estrategia de respaldos en Markdown | `module-05/CORE-MOD5-15-respaldos.md` | `validate-CORE-MOD5-15.sh` |

## Uso

```bash
# Validar todos los retos de un estudiante
labs/scripts/validate_all.sh alumno-001

# Validar un reto específico
labs/scripts/validators/module-01/validate-CORE-MOD1-01.sh alumno-001
```

## Verificación de firma

```bash
# Registrar reto completado
python3 labs/scripts/lab_state_manager.py \
  --student-id alumno-001 \
  --challenge-id CORE-MOD1-01 \
  --status PASSED

# Exportar firma de progreso
python3 labs/scripts/lab_state_manager.py \
  --student-id alumno-001 \
  --export /tmp/firma-progreso.md
```
