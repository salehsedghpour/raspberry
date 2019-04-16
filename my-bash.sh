#!/bin/bash
echo synching with git.
(cd /opt/codes/ ;git pull origin master)
#(sudo -s ; apt install python3-pip)
#/usr/bin/pip3 install requests
#pip3 install pymongo
#echo { "zone":1, "user":"me","mongo-user":"my-mongo-user", "mongo-password":"NGEyY2IwZWQ5OGM1", "mongo-url":"mon.hcsone.net:2717/" } > /opt/auth.json
/usr/bin/python3.5 /opt/codes/send_log.py
