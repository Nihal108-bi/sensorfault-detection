from pymongo import MongoClient
import pandas as pd
import json

# URI and client creation
uri="mongodb+srv://nihaljaisawal1:mrnj123@cluster0.8knpq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connectt to server
client = MongoClient(uri)

# Continue with database and collection setup as before
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"

df = pd.read_csv(r"C:\Users\Lenovo\Desktop\SensorProject\notebooks\src\wafer.csv")
df = df.drop("Unnamed: 0", axis=1)
json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
print("Data inserted successfully.")
