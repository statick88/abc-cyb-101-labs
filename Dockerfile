# Dockerfile — Entorno Kali Linux para Laboratorios ABC-CYB-101
FROM kalilinux/kali-rolling:latest

LABEL maintainer="Abacom Capacitación y Servicios Informáticos"
LABEL description="Entorno de laboratorio para Fundamentos de Ciberseguridad ABC-CYB-101 v2.1"

# Evitar prompts interactivos durante instalación
ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8

# Crear estructura de directorios de laboratorio
RUN mkdir -p /home/kali/cybersec-lab \
    /var/lab-state \
    /usr/local/bin/menu_labs \
    /usr/local/lib/lab_state_manager.py

# Instalar paquetes base y herramientas de laboratorio
# Incluye: firewall, criptografía, logging, análisis de red, hardening
RUN apt-get update -qq && \
    apt-get install -y -qq \
      kali-tools-top10 \
      nmap \
      netcat-openbsd \
      gobuster \
      dirb \
      hydra \
      john \
      sqlmap \
      metasploit-framework \
      wireshark \
      tcpdump \
      openssh-client \
      python3-pip \
      curl \
      wget \
      dnsutils \
      ufw \
      iptables \
      openssl \
      rsyslog \
      auditd \
      logrotate \
      sudo \
      whiptail \
      dialog \
      git \
      vim \
      less \
      jq \
      bc \
      coreutils \
      findutils \
      procps \
      lsof \
      net-tools \
      iproute2 \
      systemd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiar scripts de laboratorio
COPY --chown=kali:kali labs/scripts/menu_labs /usr/local/bin/menu_labs
COPY --chown=kali:kali labs/scripts/lab_state_manager.py /usr/local/lib/lab_state_manager.py
COPY --chown=kali:kali labs/scripts/validate_all.sh /usr/local/bin/validate_all.sh
COPY --chown=kali:kali labs/scripts/validators /opt/labs/validators
RUN chmod +x /usr/local/bin/menu_labs /usr/local/bin/validate_all.sh \
    && find /opt/labs/validators -name '*.sh' -exec chmod +x {} \;

# Configurar directorio de laboratorio con permisos correctos
RUN chown -R kali:kali /home/kali/cybersec-lab /var/lab-state

# Exponer puertos de servicios de laboratorio (noVNC)
EXPOSE 8080

# Cambiar a usuario kali
USER kali
WORKDIR /home/kali

# Iniciar bash por defecto
CMD ["bash"]
