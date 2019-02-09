#!/bin/bash

# rimuovo accessi vecchi se voglio..
#rm -f accessi_tracciati.log

touch ltrace_log.txt #tmp
touch accessi_tracciati.log

#compilo file accesso irregolare
gcc accesso_var.c -o accessoVar

# traccio l'andamento con ltrace
ltrace -b -o ltrace_log.txt ./accessoVar 

#cerco la riga relativa al tentativo di apertura del file
fopens=$(more ltrace_log.txt | grep fopen)

full_path=$(echo $fopens| awk -F'"' '{print $2}') #prendo il secondo campo della fopen con virgolette

folder=$(echo $full_path|cut -c1-4) #prendo solo l'indirizzo di /var a prescindere dal resto

if [[ $(stat -c %U $folder) == $(whoami) ]]; then # se il proprietario di var è lo stesso di chi tenta di accedere allora ok
    echo "Accesso regolare: "$folder" $(date)" >> accessi_tracciati.log
else
    echo "Accesso NON regolare: "$folder" $(date)" >> accessi_tracciati.log
fi

rm -f ltrace_log.txt
