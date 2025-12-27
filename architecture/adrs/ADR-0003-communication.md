# ADR-0003: Comunicación Asíncrona para IoT

## Estado
Aceptado

## Contexto
Los dispositivos IoT envían datos de forma constante y
no deben depender de disponibilidad inmediata del backend.

## Decisión
Se utiliza comunicación asíncrona mediante un broker de
mensajes (MQTT / Event Bus) para desacoplar productores
y consumidores.

## Alternativas Consideradas
- HTTP polling
- WebSockets directos

## Consecuencias
### Positivas
- Alta tolerancia a fallos
- Escalabilidad masiva
- Mejor manejo de picos de datos

### Negativas
- Complejidad en trazabilidad
- Necesidad de monitoreo de colas
