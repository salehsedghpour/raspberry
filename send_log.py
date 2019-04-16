#import sqlite3,requests,pymongo,json,time
#from requests.auth import HTTPDigestAuth
#local_db_name = '/opt/miner.db'
import pymongo,time

def send_log_to_mongo(user,zone,mongo_user,mongo_pass,mongo_url,data,miner_id):
    try:
        myclient = pymongo.MongoClient("mongodb://" + mongo_user + ":" + mongo_pass + "@" + mongo_url)
        mydb = myclient["monitoring"]
        mycol = mydb['vahid']
        mydict = {"username" : 'vahid',
        "zone_id" : 1,
        "miner_id" : 1,
        "timestamp" : time.time()}
        #"log" :data}
        x = mycol.insert_one(mydict)
    except:
        print("There is some error in sending data to miner")


#with open('/opt/auth.json', 'r') as myfile:
#    data=myfile.read()

# parse file
#obj = json.loads(data)

#for item in get_miners_list():
#    data = get_data_from_miner(item)
data = []
#send_log_to_mongo(obj['user'],obj['zone'],obj['mongo-user'],obj['mongo-password'],obj['mongo-url'],data,item[3])
send_log_to_mongo('vahid',2,'my-mongo-user','NGEyY2IwZWQ5OGM1','mon.hcsone.net:21117',data,3)

