#!/bin/bash
echo synching with git.
(cd /opt/codes/ ;git pull origin master)
(sudo -s ; apt install python3-pip)
/usr/bin/pip3 install requests
