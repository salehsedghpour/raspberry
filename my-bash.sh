#!/bin/bash
echo synching with git.
(cd /opt/codes/ ;git pull origin master)
timedatectl set-timezone Asia/Tehran
#(sudo -s ; apt install python3-pip)
#(sudo -s ; rm /opt/miner.db)
#pip3 install requests
#pip3 install pymongo
echo '{ "zone":1, "user":"vahid","mongo-user":"my-mongo-user", "mongo-password":"NGEyY2IwZWQ5OGM1", "mongo-url":"mon.hcsone.net:27117/" }' > /opt/auth.json
/usr/bin/python3.5 /opt/codes/synch_db.py
/usr/bin/python3.5 /opt/codes/send_log.py
