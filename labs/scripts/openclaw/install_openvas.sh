#!/bin/bash
# install_openvas.sh
# Instalacion de OpenVAS via Docker para escaneo de vulnerabilidades
# Nivel: Medio

set -e

echo "=== Instalando OpenVAS ==="

# Pull imagen oficial
docker pull atomicorp/openvas:latest

# Crear red dedicada
docker network create openvas_net 2>/dev/null || true

# Iniciar contenedor
docker run -d \
    --name openvas \
    --network openvas_net \
    -p 9390:9390 \
    -p 9391:9391 \
    -e OV_PASSWORD=ChangeMe123! \
    -e OV_SCAN_NET="0.0.0.0/0" \
    atomicorp/openvas:latest

# Esperar inicializacion
echo "Esperando inicializacion (60s)..."
sleep 60

# Verificar estado
echo ""
echo "=== Logs recientes ==="
docker logs openvas | tail -20

echo ""
echo "=== OpenVAS Listo ==="
echo "Interfaz: https://localhost:9390"
echo "Usuario: admin"
echo "Password: ChangeMe123!"
echo ""
echo "IMPORTANTE: Cambia la password despues del primer login"
