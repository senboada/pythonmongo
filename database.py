from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi

MONGO_URI = 'mongodb+srv://clase:Colombia2022@cluster0.zj8owbo.mongodb.net/?retryWrites=true&w=majority'
#MONGO_URI = 'mongodb+srv://userclase:KZ76mYeEHpw2bMrL@cluster0.etwsrvg.mongodb.net/?retryWrites=true&w=majorit'
ca = certifi.where()

def dbConnection():
    try:
        #client = MongoClient(MONGO_URI, tlsCAFile=ca)
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
