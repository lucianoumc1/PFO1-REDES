import socket
import threading
import sqlite3
from datetime import datetime

# Inicializar base de datos
def inicializar_bd():
    try:
        conn = sqlite3.connect("messages.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS mensajes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            contenido TEXT,
                            fecha_envio DATETIME,
                            ip_cliente TEXT)''')
        conn.commit()
        conn.close()
        print("Base de datos inicializada correctamente")
    except sqlite3.Error as e:
        print(f"Error al inicializar la BD: {e}")

# Guardar mensaje en la base
def guardar_mensaje(contenido, ip):
    try:
        conn = sqlite3.connect("messages.db")
        cursor = conn.cursor()
        fecha_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) VALUES (?, ?, ?)",
                       (contenido, fecha_envio, ip))
        conn.commit()
        conn.close()
        return fecha_envio
    except sqlite3.Error as e:
        print(f"Error al guardar mensaje: {e}")
        return None

# Manejar conexión con cliente
def manejar_cliente(conn, addr):
    print(f"Conexion establecida con {addr}")
    while True:
        try:
            data = conn.recv(1024).decode("utf-8")
            if not data or data.lower() == "exito":
                print(f"Cliente {addr} desconectado")
                break
            fecha = guardar_mensaje(data, addr[0])
            if fecha:
                respuesta = f"Mensaje recibido: {fecha}"
                conn.sendall(respuesta.encode("utf-8"))
        except Exception as e:
            print(f"Error con cliente {addr}: {e}")
            break
    conn.close()

# Inicializar servidor
def iniciar_servidor():
    inicializar_bd()
    server_socket = None
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", 5000))
        server_socket.listen(5)
        print("Servidor iniciado en localhost:5000")
        print("Esperando conexiones...")

        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=manejar_cliente, args=(conn, addr))
            thread.start()

    except OSError as e:
        print(f"Error con el socket: {e}")
    except KeyboardInterrupt:
        print("\nServidor detenido manualmente")
    finally:
        if server_socket:
            server_socket.close()

if __name__ == "__main__":
    iniciar_servidor()
