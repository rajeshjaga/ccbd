#!/bin/bash
sudo rm -r /opt/basebuild
sudo git clone https://github.com/nikithgowda22/LABSP /opt/basebuild
sudo rm -rf /home/rit-cse/.bash_history
nohup sh -c 'sleep 3 && rm -f /home/rit-cse/.bash_history' & disown && exit