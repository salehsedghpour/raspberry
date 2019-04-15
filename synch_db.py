import sqlite3,pymongo,json

local_db_name = '/opt/miner.db'

def initiate_db():
    try:
        conn = sqlite3.connect(local_db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE miners
                     (miner_id real, ip text, zone_id real,user text, pass text)''')

    except:
        print("Miner DB is already initiated.")

def get_ip_from_mongo(username,zone_id,mongo_user,mongo_pass,mongo_url):
    try:
        myclient = pymongo.MongoClient("mongodb://"+mongo_user+":"+mongo_pass+"@"+mongo_url)
        mydb = myclient["monitoring"]
        mycol = mydb["configurations"]
        out = []
        for item in mycol.find({"username" : username}):
            for id in item['zones']:
                if id['id'] == zone_id:
                    for miner in id['miner_list']:
                        out.append([miner['ip'],miner['id'],miner['user'],miner['pass']])
        return(out)

    except:
        print('There is some Error in collecting data from mongo configuration')
        return []

def add_new_miner_to_local_db(ip,zone_id):
    try:
        conn = sqlite3.connect(local_db_name)
        c = conn.cursor()
        c.execute("INSERT INTO miners(miner_id,ip,zone_id,user,pass) SELECT "+ str(ip[1])+",'"+ str(ip[0])+"',"+ str(zone_id)+",'"+str(ip[2])+"','"+str(ip[3])+"'"+" WHERE NOT EXISTS(SELECT 1 FROM miners WHERE miner_id= "+str(ip[1])+" AND ip = '"+str(ip[0])+"' AND zone_id ="+ str(zone_id)+" AND user='"+str(ip[2])+"' AND pass= '"+str(ip[3])+"'"+")")
        conn.commit()
        conn.close()
    except:
        print("Something Happend")


with open('/opt/auth.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)


initiate_db()

for item in get_ip_from_mongo(obj['user'],obj['zone'],obj['mongo-user'],obj['mongo-password'],obj['mongo-url']):
    add_new_miner_to_local_db(item,1)
