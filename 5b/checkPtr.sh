#!/bin/bash

#rimuovo accessi vecchi se voglio..
#rm -f accessi_tracciati.log

touch strace_log.txt # temp log
touch accessi_tracciati.log

#compilo file accesso irregolare
gcc accesso_random.c -o accessoRandom

# traccio l'andamento con ltrace
strace -o strace_log.txt ./accessoRandom 

#cerco la riga relativa al tentativo di accesso a memoria (è il caso di core dump)
accessoMem=$(more strace_log.txt | grep SIGSEGV | grep si_addr)

indirizzo=$(echo $accessoMem| awk -F'=' '{print $4}'| cut -c1-9) 
#prendo solo l'indirizzo di memoria.

echo "Accesso all'indirizzo di memoria: "$indirizzo" $(date)" >> accessi_tracciati.log

# the temp log is removed
rm -f strace_log.txt
