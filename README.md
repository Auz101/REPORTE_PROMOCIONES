# Reporte Promociones API

API creada con Flask para recibir solicitudes de generación de reportes de promociones.

## Endpoints

- **GET /** → Verifica si el servidor está activo.
- **POST /generar_reporte** → Recibe parámetros `email` y `promotion_code`.

Ejemplo:
```json
{
  "email": "usuario@empresa.com",
  "promotion_code": "PROMO123"
}
