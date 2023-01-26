#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
int c_socket;
struct sockaddr_in serverAddress;
int random_Num;

// Create Socket
c_socket = socket(AF_INET, SOCK_STREAM, 0);

// Configure Address
serverAddress.sin_family = AF_INET;
serverAddress.sin_port = htons(8080);
serverAddress.sin_addr.s_addr = inet_addr("192.168.100.212");


// Connect To Server
connect(c_socket, (struct sockaddr *) &serverAddress, sizeof(serverAddress));

// Receiving Number From Server
recv(c_socket, &random_Num, sizeof(random_Num), 0);

// Print Out Number
printf("Random Number: %d\n", random_Num);

// Close Client's Socket
close(c_socket);

return 0;
}
