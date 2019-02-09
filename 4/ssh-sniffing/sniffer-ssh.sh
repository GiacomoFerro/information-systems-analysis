#!/bin/bash

# eseguirlo dopo open-ssh prima di inserire la password di localhost!

# traccio le chiamate
ssh_pid=$(ps -elf | grep "priv" | grep "root"|awk '{print $4}')
sudo strace -o ssh.log -p $(echo $ssh_pid | awk '{print $1}')

echo "digita password da mostrare:"
read -s pass

# stampa del risultato filtrato
cat ssh.log | grep $pass





