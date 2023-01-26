#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main() {
int s_socket, c_socket, random_Num;
struct sockaddr_in serverAddress, c_address;
int clientAddressLength = sizeof(c_address);

// Create Socket
s_socket = socket(AF_INET, SOCK_STREAM, 0);
if (s_socket == -1){
        printf("Created socket Failed...\n");
        exit(0);
}
else
printf("Created socket Success...\n");
        bzero(&serverAddress, sizeof(serverAddress));

// Configure Address
serverAddress.sin_family = AF_INET;
serverAddress.sin_port = htons(8080);
serverAddress.sin_addr.s_addr = INADDR_ANY;

// Bind Socket To Address
if((bind(s_socket, (struct sockaddr *) &serverAddress, sizeof(serverAddress))) >
        printf("Socket Failed To Bind...\n");

}
else
        printf("Socket Success Bind...\n");

// Listen Incoming Connections
if((listen(s_socket, 5)) != 0) {
        printf("Listening Failed...\n");
}
else
        printf("Listening...\n");

while (1) {
// Accept Incoming Connection
c_socket = accept(s_socket, (struct sockaddr *) &c_address,
&clientAddressLength);
if(c_socket < 0){
        printf("Connected Failed...\n");

}
else
        printf("Connected...\n");

// Random Number Will Generate
srand(time(0));
random_Num = rand() % 900 + 100;

//Random Number Will Be Send To Client
send(c_socket, &random_Num, sizeof(random_Num), 0);

// Closing Socket's Client
close(c_socket);
}

// Closing Socket's Server
close(s_socket);

return 0;
}
