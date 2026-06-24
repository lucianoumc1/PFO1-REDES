import socket

# Conectar al servidor
def conectar_servidor():
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(("localhost", 5000))
        print("Conectado al servidor localhost:5000")

        while True:
            mensaje = input("Tu: ")
            if mensaje.lower() == "exito":
                cliente.sendall(mensaje.encode("utf-8"))
                break
            cliente.sendall(mensaje.encode("utf-8"))
            respuesta = cliente.recv(1024).decode("utf-8")
            print(f"Servidor: {respuesta}")

        cliente.close()
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor. Asegurate de que esta en ejecucion.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    conectar_servidor()
