# ABC-CYB-101 Labs

Motor de laboratorios CORE para **Fundamentos de Ciberseguridad ABC-CYB-101**.
Este repositorio es autocontenido: clónelo y ejecútelo sin dependencias del curso principal.

## Resultado

- **60 retos CORE** organizados en 5 módulos.
- **CLI interactivo** (`menu_labs`) con navegación por módulos y validación automática.
- **Persistencia firmada**: estado por estudiante en `/var/lab-state/progress/` con HMAC-SHA256.
- **Stack SIEM opcional**: Loki + Promtail + Grafana mediante perfil `siem`.

## Inicio rápido

```bash
git clone https://github.com/statick88/abc-cyb-101-labs.git
cd abc-cyb-101-labs

# Iniciar entorno base
docker compose up -d

# Iniciar con SIEM
docker compose --profile siem up -d

# Acceder a Kali
docker compose exec kali bash

# Dentro del contenedor
sudo menu
validate_all.sh alumno-001
```

## Estructura

| Ruta | Propósito |
|------|-----------|
| `docker-compose.yml` | Orquestación: Kali, DVWA, Metasploitable2, SIEM |
| `Dockerfile` | Imagen Kali con herramientas de seguridad |
| `labs/scripts/menu_labs` | CLI interactivo |
| `labs/scripts/lab_state_manager.py` | Gestión de estado y firma HMAC |
| `labs/scripts/validate_all.sh` | Validador maestro |
| `labs/scripts/validators/module-01/` a `module-05/` | 60 validadores automáticos |
| `labs/spec/state-schema-and-taxonomy.md` | Especificación de estado y taxonomía |
| `labs/spec/challenge-mapping-matrix.md` | Mapeo reto → archivo → validador |
| `rubricas_evaluacion_ABC-CYB-101.md` | Rúbricas 30/40/30 |

## Esquema de estado

```
/var/lab-state/progress/<student_id>/
├── index.json                 # Índice global del estudiante
├── CORE-MOD1-01.json          # Registro individual con firma HMAC
└── firma-progreso-YYYYMMDD.txt # Exportación para entrega
```

## Requisitos

- Docker Engine 24.0+
- Docker Compose 2.20+
- 8 GB RAM recomendados (4 GB mínimos)

## Licencia

Privado — Abacom Capacitación y Servicios Informáticos
