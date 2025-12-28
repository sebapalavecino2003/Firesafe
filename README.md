# FireSafe 🔥

FireSafe es un sistema de monitoreo y prevención de incendios basado en una
arquitectura de microservicios, diseñado con FastAPI, Docker y JWT.

## Arquitectura
- API Gateway como punto único de entrada
- Microservicios independientes
- Autenticación centralizada con JWT
- Orquestación con Docker Compose

## Servicios
- api-gateway
- auth-service
- device-service
- alert-service
- data-service
- notification-service

## Ejecución local

```bash
docker compose build
docker compose up
