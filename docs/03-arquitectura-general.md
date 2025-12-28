# ARQUITECTURA GENERAL

FireSafe adopta una arquitectura basada en microservicios, donde cada servicio cumple una responsabilidad
bien definida y se comunica mediante HTTP sobre una red interna.

Un API Gateway actúa como punto único de entrada, centralizando la autenticación, la validación de tokens
y el enrutamiento de solicitudes hacia los servicios internos.
