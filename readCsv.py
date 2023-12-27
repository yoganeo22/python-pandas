import pandas as pd 

# read csv data
csvFile = "data/csvData.csv"
res = pd.read_csv(csvFile)
print(res)
