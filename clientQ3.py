import socket
def main():
    #IP and port of the server
    s_ip = "192.168.100.212"
    s_port = 8080

    # Create socket
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    c.connect((s_ip, s_port))

    # Request a quote from server
    quote = c.recv(1024)
    print("                    THE QUOTES OF THE DAY!                     ")
    print("_________")
    print("THE QUOTES FOR THIS SESSION>>> %s" % quote.decode())

    # Close socket
    c.close()
