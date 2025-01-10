# A program that generate centripetal forces of experimental data from Excel files as a plot and linear regression line graph at once
# Data excel files automatically store time(s), angle(rad), angular speed(rad/s), angular acceleration(rad/s²), and force(N) by run

#import pandas module to read excel file
#import matplotlib module to make graph
#import scipy module to use linear regression
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Excel file list
file_names = ["C:/Users/danie/OneDrive/바탕 화면/python workspace/data/8cm.xlsx",
              "C:/Users/danie/OneDrive/바탕 화면/python workspace/data/11cm.xlsx",
              "C:/Users/danie/OneDrive/바탕 화면/python workspace/data/14cm.xlsx",
              "C:/Users/danie/OneDrive/바탕 화면/python workspace/data/17cm.xlsx"]
# Name, Color list
names = ["8cm", "11cm", "14cm", "17cm"]
colors = ['red', 'blue', 'green', 'orange']

merged_data = pd.concat([pd.read_excel(file, engine='openpyxl') for file in file_names], ignore_index=True)

# Eliminate outlier
merged_data = merged_data[(merged_data['Angular Speed (rad/s) Run #1'] > 0) & (merged_data['Angular Speed (rad/s) Run #1'] < 8)]

# Read excel file
for i, file in enumerate(file_names):
    data = pd.read_excel(file, engine='openpyxl')
    data = data[(data['Angular Speed (rad/s) Run #1'] > 0) & (data['Angular Speed (rad/s) Run #1'] < 8)]
    # Make scatter plot (black edgecolors, colored by colors list, size 10, label by names list)
    plt.scatter(data['Angular Speed (rad/s) Run #1'], data['Force (N) Run #1'], 
            edgecolors='black', linewidth=1, facecolors=colors[i], s=10, label=names[i])
    # Add linear regression graph (line colored by colors list(same as scatter plot), set linewidth as 2)
    slope, intercept,_,_,_ = stats.linregress(data['Angular Speed (rad/s) Run #1'], data['Force (N) Run #1'])
    x = data['Angular Speed (rad/s) Run #1']
    plt.plot(x, intercept + slope*x, color=colors[i], linewidth=2)

# Set axis name, graph name, add legend
plt.xlabel('Angular Speed (rad/s)')
plt.ylabel('Force (N)')
plt.legend()

# Save as png file
plt.savefig("C:/Users/danie/OneDrive/바탕 화면/python workspace/data/graph.png")
# Show graph
plt.show()
