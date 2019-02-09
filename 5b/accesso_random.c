#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main(){

    srand(time(NULL));

    int *p;

    p=(int *)rand();

    //tento di accedere all'indirizzo di memoria dato
    *p=5;

}
