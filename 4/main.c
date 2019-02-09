#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){

    pid_t ID;

    //script finale di lancio
    ID=fork();

	if(ID==-1){
    	puts("errore nella fork");
		exit(1);
	}
	if(ID==0){
    	execlp("./sysAnalysis.sh","",NULL);
		printf("exec fallita\n");
	}
	if(ID!=0){
    	wait(NULL); //sono il padre ed aspetto il figlio
	}

}
