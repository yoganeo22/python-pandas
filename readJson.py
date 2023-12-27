import pandas as pd 

# read json data
jsonFile = "data/jsonData.json"
res = pd.read_json(jsonFile, orient='index')
print(res)
