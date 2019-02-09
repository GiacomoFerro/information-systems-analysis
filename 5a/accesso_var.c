#include <stdio.h>

int main(void) {

    FILE * fd = NULL;

    fd = fopen("/var/prova.txt", "w"); //NULL se non va a buon fine
      
    fd = fopen("/var/prova.txt", "w"); //NULL se non va a buon fine
    fprintf(fd,"%s","tentativo di scrittura");   
  
    fclose(fd);

}
