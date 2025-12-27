# PLAYBOOK — CREACION DE MICRO-SERVICIO

## OBJETIVO
Definir el proceso estándar para crear un nuevo micro-servicio.

## PASOS
1. Crear carpeta del servicio
2. Definir responsabilidad unica
3. Crear API base /health
4. Definir base de datos propia
5. Documentar API (OpenAPI)
6. Registrar eventos que consume/emite

## REGLAS
- Un servicio = un dominio
- No compartir bases de datos
- No llamar directo a otro servicio sin contrato

## CHECKLIST
- [ ] API documentada
- [ ] Healthcheck disponible
- [ ] Logs habilitados
- [ ] Configuracion por entorno
