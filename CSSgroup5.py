import matplotlib.pyplot as plt
import math
import numpy as np
def chartresult(sizes,charttype):
    labels = 'Excellent', 'Very Good', 'Good', 'Average','Poor'
    #sizes = [215, 130, 245, 210,220]
    #colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','white']
    colors = ['red', 'green', 'blue', 'yellow', 'purple']
    if(charttype=="pie"):
        explode = (0, 0, 0, 0, 0)  # explode 1st slice
        plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct='%1.1f%%', shadow=False, startangle=140)
        plt.axis('equal')
        #plt.bar(heights,sizes,width,color ='blue')
        plt.show()
    elif(charttype == "bar"):
        height = range(len(sizes))
        percentvalue = []
        for i in sizes:
            percent = (i/(sum(sizes))) * 100
            percent = round(percent,2)
            percentvalue.append(percent)
        width = 0.8
        x_pos = np.arange(len(labels))
        y_pos = np.arange(len(labels))
        plt.bar(height, sizes, width, color = colors, label = labels)
        plt.xticks(x_pos,labels)
        plt.show()

filename = "/home/python/Desktop/DATASCIENCE/cybergroup5.csv"
def ReadCsv(filename):
    import csv
    excellent, vg, good, avg ,poor = [],[],[],[],[]
    with open(filename,'r') as file:
        reader = csv.reader(file)
        for rows in reader:
            excellent.append(rows.count("Excellent"))
            vg.append(rows.count("Very Good"))
            good.append(rows.count("Good"))
            avg.append(rows.count("Average"))
            poor.append(rows.count("Poor"))
        excellent,vg,good,avg,poor = sum(excellent),sum(vg),sum(good),sum(avg),sum(poor)

    file.close()
    chartresult([excellent,vg,good,avg,poor],"pie") #for PIECHART
    chartresult([excellent,vg,good,avg,poor],"bar")
ReadCsv(filename)
