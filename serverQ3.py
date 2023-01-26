import random
import threading
import socket

#array of quotes
quotes = ["Imagination is useful as a plan or a fantasy. But the only thing you>
,
"Conscious action does not produce karma – instinctive reaction does.",
"I am not here to solace you. I am here to awaken you."]

#random quotes from array and send to client
def handle_client(sockfd):
    quote = random.choice(quotes)
    s.sendall(quote.encode())
    s.close()

def main():
    #server ip and port
    bind_ip = "192.168.100.212"
    bind_port = 8080
 #create and bind socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((b_ip, b_port))

    #listen for client
    s.listen(5)
    print(" LISTENING From client on : %s:%d" % (b_ip, b_port))

    #start connections and execute handle_client function
    while True:
        client, addr = s.accept()
        print("Successful to connect : %s" % str(addr))
        client = threading.Thread(target=handle_client, args=(client,))
        client.start()


main()
