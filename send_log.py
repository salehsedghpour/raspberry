import sqlite3,requests,pymongo,json,time
from requests.auth import HTTPDigestAuth
local_db_name = '/opt/miner.db'


def get_miners_list():
    try:
        conn = sqlite3.connect(local_db_name)
        c = conn.cursor()
        c.execute("SELECT ip,user,pass,miner_id FROM miners")
        out = []
        for item in c.fetchall():
            out.append(item)
        return out
    except:
        print("There is some Error in getting data from sqlite")

def get_data_from_miner(ip):
    try:
        url = "/cgi-bin/get_miner_status.cgi"
        my_url = "https://jigsaw.w3.org/HTTP/Digest/"
        #r= requests.get(my_url,auth=HTTPDigestAuth("guest","guest"))
        r =requests.get("http://"+ip[0]+url, auth=HTTPDigestAuth(ip[1], ip[2]))
        #r.content.
        out_put = r.content.decode('utf8')
        out = json.loads(out_put)
        return out
    except:
        print("there is some error in getting data from miner.")

def send_log_to_mongo(user,zone,mongo_user,mongo_pass,mongo_url,data,miner_id):
    try:
        myclient = pymongo.MongoClient("mongodb://" + mongo_user + ":" + mongo_pass + "@" + mongo_url)
        mydb = myclient["monitoring"]
        mycol = mydb[user]
        mydict = {"username" : user,
        "zone_id" : zone,
        "miner_id" : int(miner_id),
        "timestamp" : time.time()+16200,
        "log" :data}
        x = mycol.insert_one(mydict)
    except:
        print("There is some error in sending data to miner")


with open('/opt/auth.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

for item in get_miners_list():
#item = ['192.168.1.56','root','root']
    data = get_data_from_miner(item)
#data = []
    if data != None:
        send_log_to_mongo(obj['user'],obj['zone'],obj['mongo-user'],obj['mongo-password'],obj['mongo-url'],data,item[3])
