# C4 – CONTEXT DIAGRAM

## System
Plataforma de Monitoreo Inteligente (PMI)

## Purpose
Centralizar datos de sensores IoT, detectar eventos de riesgo
y notificar a los usuarios en tiempo real mediante una
aplicación web.

## Users
- Usuario Final
- Administrador

## External Systems
- Dispositivos IoT (ESP32 / Arduino)
- Servicio de Notificaciones (Email / Push / Telegram)
- Navegador Web

## Relationships
- Los dispositivos IoT envían datos al sistema
- El sistema procesa y evalúa riesgos
- Los usuarios interactúan vía web
- Las alertas se envían mediante servicios externos
