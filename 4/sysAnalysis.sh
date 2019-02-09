#!/bin/bash

#rm -f writes.log forks.log


gcc fork.c -o fork
strace -o dump.txt -ff ./fork

pids=($(ls | grep "dump.txt" | cut -d'.' -f3)) #prendo i pids


pidPadre=${pids[0]} # salvo il pid del padre ipotetico
for i in ${pids[@]}; do
    if [ $i -lt $pidPadre ]; then
        pidPadre=$i
    fi
done

#ora pidPadre avrà pid del padre...procedo ad analizzare le fork fatte (clone)

# analizzo le fork fatte dal padre
f_dump="dump.txt.$pidPadre"
pidFigli=($(cat $f_dump | grep clone | awk -F ' = ' '{print $2}')) # mi salvo la "lista" dei pids dei figli
if [ ${#pidFigli[@]} -ne 0 ]; then
    echo "numero di figli fatti: "${#pidFigli[@]} > forks.log
    for i in ${pidFigli[@]}; do
        echo "pid del figlio: "$i >> forks.log
    done
else
    echo "non sono state fatte fork." >> forks.log
fi

# ora analizzo le scritture nelle pipe fatte dal padre
writes=$(cat $f_dump | grep write | awk -F "[()]" '{print $2}'| cut -d ',' -f1)

for i in ${writes[@]}; do
    if [ $i -gt 2 ]; then
        echo "$(date): processo padre scrive al figlio su descrittore $i." >> writes.log
    fi
done

#N.B. abbiamo fatto una fork sola e una pipe sola.
#Descittore input come 3 e come output 4 dal momento che 0,1,2 sono descrittori occupati per standard input, output ed error.


#tolgo i dumps
rm -f dump.txt.*




