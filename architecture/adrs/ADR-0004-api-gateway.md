# ADR-0004: Uso de API Gateway (BFF)

## Estado
Aceptado

## Contexto
El frontend no debe conocer la estructura interna
de los micro-servicios.

## Decisión
Se introduce un API Gateway como punto único de entrada,
encargado de seguridad, orquestación y versionado.

## Consecuencias
- Menor acoplamiento frontend-backend
- Centralización de seguridad
- Punto único de control
