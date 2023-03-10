import socket

def convert_to_celsius(fahren):
    cels = (fahren - 32) * 5 / 9
    return cels

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 8080))
    s.listen(1)

    print("Server is waiting for  connections...")

    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
		fahren = float(data.decode())
            	cels = convert_to_celsius(fahren)
            	conn.send(str(cels).encode())
        conn.close()

if __name__ == '__main__':
    main()
