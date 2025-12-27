# RUNBOOK — SERVICIO CAIDO

## SINTOMA
El frontend no responde o muestra error 5xx.

## IMPACTO
Usuarios no pueden operar el sistema.

## PASOS DE DIAGNOSTICO
1. Verificar healthcheck del servicio
2. Revisar logs
3. Ver estado de la base de datos
4. Verificar consumo de recursos

## ACCIONES
- Reiniciar servicio
- Escalar instancia
- Activar modo degradado

## PREVENCION
- Monitoreo de healthchecks
- Alertas por CPU/Memoria
