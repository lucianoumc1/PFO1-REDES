# Chat Cliente-Servidor con Sockets

## Descripción

Aplicación de chat en consola desarrollada en **Python** mediante sockets TCP/IP. Varios clientes pueden enlazarse a un servidor central, que recibe cada mensaje, lo registra en **SQLite** y devuelve una confirmación de recepción.

---

## Estructura del Proyecto

```
chat-cliente-servidor/
├── server.py          # Servidor de chat con sockets y base de datos
├── client.py          # Cliente de chat en consola
├── messages.db        # Base de datos SQLite (se crea automáticamente)
└── README.md          # Documentación del proyecto
```

---

## Esquema de Base de Datos

La base de datos SQLite contiene una tabla llamada `mensajes` con los siguientes campos:

| Campo        | Tipo     | Descripción                           |
|--------------|----------|---------------------------------------|
| id           | INTEGER  | Identificador único autoincremental   |
| contenido    | TEXT     | Contenido del mensaje enviado         |
| fecha_envio  | DATETIME | Fecha y hora en que se envió el mensaje |
| ip_cliente   | TEXT     | Dirección IP del cliente              |

---

## Requisitos

- Python 3.6 o superior
- Librerías estándar de Python:
  - `socket`
  - `sqlite3`
  - `threading`
  - `datetime`

---

## Instalación y Uso

1. **Clonar o descargar el proyecto**
   ```bash
   git clone https://github.com/lucianoumc1/PFO1-REDES.git
   cd chat-cliente-servidor
   ```

2. **Ejecutar el servidor**

   En una terminal:
   ```bash
   py ./server.py
   ```

   Salida esperada:
   ```
   Base de datos inicializada correctamente
   Servidor iniciado en localhost:5000
   Esperando conexiones...
   ```

   Cuando un cliente se conecta, el servidor muestra:
   ```
   Conexion establecida con ('127.0.0.1', <puerto>)
   ```

3. **Ejecutar el cliente**

   En otra terminal:
   ```bash
   py ./client.py
   ```

   Salida esperada:
   ```
   Conectado al servidor localhost:5000
   Tu:
   ```

4. **Enviar mensajes**

   - Escribe un mensaje en el cliente y presiona Enter.
   - El servidor recibe el mensaje, lo guarda en la base de datos y responde con un timestamp.
   - El cliente muestra la confirmación recibida.
   - Escribe `exito` para cerrar la conexión.

   Ejemplo de intercambio:
   ```
   Tu: Hola
   Servidor: Mensaje recibido: 2026-06-25 14:30:00
   Tu: exito
   ```