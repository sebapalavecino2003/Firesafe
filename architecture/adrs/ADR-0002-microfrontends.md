# ADR-0002: Uso de Micro-frontends

## Estado
Aceptado

## Contexto
La aplicación web contiene dominios funcionales diferenciados
(dashboard, dispositivos, alertas, administración) que deben
poder evolucionar de forma independiente.

## Decisión
Se adopta un enfoque de micro-frontends, con un contenedor
principal (shell) que integra múltiples frontends desacoplados.

## Alternativas Consideradas
- SPA monolítica
- Múltiples SPAs independientes

## Consecuencias
### Positivas
- Despliegues independientes
- Separación clara por dominio
- Escalabilidad del frontend

### Negativas
- Mayor complejidad de integración
- Necesidad de estandarizar contratos
