#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {

    int fds[2];
    int pipe_id = pipe(fds);
    char buf[50];


    pid_t pid = fork();

    if (pid < 0) {
        printf("Errore nella fork.\n");
    }

    if (pid == 0) {
        //figlio riposa qualce secondo per consentire al padre di scrivere
        sleep(1);
        int r = read(fds[0], buf, 50);
        printf("figlio ha letto: %s", buf);
    }

    if(pid!=0){ 
        write(fds[1], "messaggio inviato dal padre.\n", strlen("messaggio inviato dal padre.\n"));
        printf("il padre ha scritto.\n");
        wait(NULL);
    }
 
}
