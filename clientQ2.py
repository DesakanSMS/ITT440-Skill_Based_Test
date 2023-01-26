import socket

def main():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(('192.168.100.212', 8080))

    fahren = float(input("Entery your temperature in Fahrenheit: "))
    c.send(str(fahren).encode())

    cels = c.recv(1024).decode()
    print(f"Your temperature in Celsius: {cels}")

    c.close()

if __name__ == '__main__':
    main()
