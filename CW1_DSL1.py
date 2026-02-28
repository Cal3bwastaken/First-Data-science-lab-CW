#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 11:16:42 2026

@author: calebpalluotto
"""
import pandas as pd
import matplotlib.pyplot as plt


# graph 1 line chart
smokingEng = pd.read_csv(r"/Users/calebpalluotto/Downloads/England_smoke.csv")
smokingWales = pd.read_csv(r"/Users/calebpalluotto/Downloads/Wales_smoke.csv")
smokingScot = pd.read_csv(
    r"/Users/calebpalluotto/Downloads/Scotland_smoke.csv")
smokingNI = pd.read_csv(r"/Users/calebpalluotto/Downloads/NI_smoke.csv")
plt.figure()
plt.plot(smokingEng["year"], smokingEng["% of smokers"], label="England")
plt.plot(smokingWales["year"], smokingWales["% of smokers"], label="Wales")
plt.plot(smokingScot["year"], smokingScot["% of smokers"], label="Scotland")
plt.plot(smokingNI["year"], smokingNI["% of smokers"], 
         label="Northern Ireland")

plt.xlabel("Years")
plt.ylabel("Percentage")
plt.ylim(10,25)
plt.title("% of smokers in England,Scotland,Wales and Northern Ireland")
plt.legend()
plt.show()

#graph 2 bar chart

def func_bar (x, y, title="My Chart"):
    """
    create a bar chart with data from a csv file

    """
    plt.bar(x, y, color="lightgreen")
    
    plt.title(title)
    plt.xlabel("Years")
    plt.ylabel("Percentage")
    plt.ylim(5,22.5)
    plt.show()

smoking = pd.read_csv(r"/Users/calebpalluotto/Downloads/smoking.csv")

func_bar(smoking["year"], smoking["smoker pop"], 
         title = '% of smokers in the UK by year')


#graph 3 pie charts

smoking2023 = np.array([[11.6, 88.4], [13.5, 86.5], [12.6, 87.4],
                        [13.3, 86.7]])
smoking2011 = np.array([[19.8, 80.2], [23.4, 76.6], [22.3, 77.7],
                        [18.9, 81.1]])
my_colorsEng = ['red','pink']
my_colorsScot = ['blue','lightblue']
my_colorsWales = ['red','lightgreen']
my_colorsNI = ['orange','lightgreen']


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle('Smoking Rates by Country (2011)', fontsize=14)



ax1.pie(smoking2011[0], labels=['Smokers','Non-Smokers'], autopct='%1.1f%%', 
        colors=my_colorsEng)
ax1.set_title('England')
ax2.pie(smoking2011[1], labels=['Smokers','Non-Smokers'], autopct='%1.1f%%',
        colors=my_colorsScot)
ax2.set_title('Scotland')
ax3.pie(smoking2011[2], labels=['Smokers','Non-Smokers'], autopct='%1.1f%%',
        colors=my_colorsWales)
ax3.set_title('Wales')
ax4.pie(smoking2011[3], labels=['Smokers','Non-Smokers'], autopct='%1.1f%%',
        colors=my_colorsNI)
ax4.set_title('N. Ireland')
plt.show()

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle('Smoking Rates by Country (2023)', fontsize=14)



ax1.pie(smoking2023[0], labels=['Smokers','Non-Smokers'], autopct='%1.1f%%', 
        colors=my_colorsEng)
ax1.set_title('England')
ax2.pie(smoking2023[1], labels=['Smokers','Non-Smokers'], autopct='%1.1f%%',
        colors=my_colorsScot)
ax2.set_title('Scotland')
ax3.pie(smoking2023[2], labels=['Smokers','Non-Smokers'], autopct='%1.1f%%',
        colors=my_colorsWales)
ax3.set_title('Wales')
ax4.pie(smoking2023[3], labels=['Smokers','Non-Smokers'], autopct='%1.1f%%',
        colors=my_colorsNI)
ax4.set_title('N. Ireland')
plt.show()
