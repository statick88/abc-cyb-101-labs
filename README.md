# ABC-CYB-101 Labs

Motor de laboratorios CORE para el curso **Fundamentos de Ciberseguridad ABC-CYB-101**.

## Estructura

```
.
├── docker-compose.yml          # Orquestación de servicios (Kali, DVWA, Metasploitable2, SIEM)
├── Dockerfile                  # Imagen base Kali Linux con herramientas de seguridad
├── rubricas_evaluacion_ABC-CYB-101.md  # Rúbricas alineadas a esquema 30/40/30
├── labs/
│   ├── scripts/
│   │   ├── menu_labs           # CLI interactivo de laboratorios (alias: sudo menu)
│   │   ├── lab_state_manager.py # Gestión de estado y firma HMAC-SHA256
│   │   ├── validate_all.sh     # Validador maestro de 60 retos CORE
│   │   ├── promtail-config.yaml # Configuración de Promtail para stack SIEM
│   │   ├── grafana-dashboards/  # Dashboards preconfigurados para Grafana
│   │   └── grafana-datasources/ # Fuentes de datos para Loki
│   ├── spec/
│   │   ├── state-schema-and-taxonomy.md  # Especificación de esquema JSON de progreso
│   │   └── challenge-mapping-matrix.md    # Matriz reto → archivo → validador
│   └── validators/
│       ├── module-01/          # 6 validadores (Módulo I)
│       ├── module-02/          # 12 validadores (Módulo II)
│       ├── module-03/          # 13 validadores (Módulo III)
│       ├── module-04/          # 14 validadores (Módulo IV)
│       └── module-05/          # 15 validadores (Módulo V)
└── .gitignore
```

## Uso rápido

```bash
# Clonar repositorio
git clone <url> abc-cyb-101-labs
cd abc-cyb-101-labs

# Iniciar laboratorios
docker compose up -d

# Acceder al contenedor Kali
docker compose exec kali bash

# Dentro del contenedor:
sudo menu                    # Menú interactivo de laboratorios
validate_all.sh alumno-001   # Validar todos los retos de un estudiante
```

## Esquema de estado

Los retos se registran en `/var/lab-state/progress/<student_id>/<challenge_id>.json` con firma HMAC-SHA256.

- **Estado por reto**: `PASSED` | `FAILED`
- **Firma**: `sha256:<hmac_hex>`
- **Exportación**: `python3 labs/scripts/lab_state_manager.py --student-id <id> --export <file>`

## Requisitos

- Docker Engine 24.0+
- Docker Compose 2.20+
- 8 GB RAM recomendados (4 GB mínimos)

## Licencia

Privado — Abacom Capacitación y Servicios Informáticos
