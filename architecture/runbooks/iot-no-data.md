# RUNBOOK — IOT SIN DATOS

## SINTOMA
No se reciben datos de sensores.

## PASOS
1. Verificar broker MQTT activo
2. Validar ultimo mensaje recibido
3. Revisar conectividad del dispositivo
4. Validar credenciales del dispositivo

## ACCIONES
- Reiniciar broker
- Reintentar conexion
- Marcar dispositivo offline

## PREVENCION
- Heartbeat de dispositivos
- Alerta por inactividad
