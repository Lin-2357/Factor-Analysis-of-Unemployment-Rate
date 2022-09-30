import matplotlib.pyplot as plt
import json

data = json.load(open("Normalized_Consumers_2003-2022.json"))

x = 'U.S. city average Purchasing power of the consumer dollar Not Seasonally Adjusted       '
y = 'U.S. city average Food and beverages Not Seasonally Adjusted       '
rowx = [float(data[x][i]) for i in data[x]]
rowy = [float(data[y][i]) for i in data[y]]

plt.plot(rowy, rowx)
plt.savefig("scratch.jpg")