#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

const char *msg = "Congratulations, you've successfully received a message from the server!\n";

int server(){

     // start by getting a random port from the ephemeral port range
    srandom(getpid()); // random seed based on this process's OS-assigned ID
    int port = 0xc000 | (random()&0x3fff); // random element of 49152–65535

    // create an address structure: IPv4 protocol, any IP address, on given port
    // note: htonl and htons are endian converters, essential for Internet communication
    struct sockaddr_in ipOfServer;
    memset(&ipOfServer, 0, sizeof(struct sockaddr_in));
    ipOfServer.sin_family = AF_INET;
    ipOfServer.sin_addr.s_addr = htonl(INADDR_ANY);
    ipOfServer.sin_port = htons(port);

    // we'll have one socket that waits for other sockets to connect to it
    // those other sockets will be the ones we used to communicate
    int listener = socket(AF_INET, SOCK_STREAM, 0);

    // and we need to tell the OS that this socket will use the address created for it
    bind(listener, (struct sockaddr*)&ipOfServer , sizeof(ipOfServer));

    // wait for connections; if too many at once, suggest the OS queue up 20
    listen(listener , 20);
    
    system("hostname -I"); // display all this computer's IP addresses
    printf("The server is now listening on port %d\n", port); // and listening port

    for(;;) {
        printf("Waiting for a connection\n");
        // get a connection socket (this call will wait for one to connect)
        int connection = accept(listener, (struct sockaddr*)NULL, NULL);
        printf("Got a connection\n");
        if (random()%2) { // half the time
            write(connection, msg, 40); // send half a message
            usleep(100000); // pause for 1/10 of a second
            write(connection, msg+40, strlen(msg+40)); // send the other half
        } else {
            write(connection, msg, strlen(msg)); // send a full message
        }
        close(connection); // and disconnect
    }

    // unreachable code, but still have polite code as good practice
    close(listener);
    return 0;

}

int client(char *ip, int port){

    struct sockaddr_in server;
    memset(&server, 0, sizeof(struct sockaddr_in));
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr(ip);
    server.sin_port = htons(port);
    
    int s;
    s = socket(AF_INET, SOCK_STREAM, 0);

    connect(s, (struct sockaddr*)&server, sizeof(server));

    char buff[100];
    read(s, buff, sizeof(buff));
}
int main(int argc, char* argv[]){

    if(argc == 1)
        server();
    
    if(argc == 2)
        server();
    if(argc == 3)
        0;
        //client(ip,);
    
    printf("%d\n",argv[1], argv[2]);
    return 0;
}
