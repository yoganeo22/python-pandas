import pandas as pd 
import matplotlib.pyplot as plt

# read csv data
csvFile = "data/csvData.csv"
res = pd.read_csv(csvFile)
print(res)

# plot line chart
res.plot(x="x-Axis", y=["Num", "Median"], linewidth=2.0)
plt.title("Average Data")
plt.show()
