import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics as st
import csv
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

populationMean = st.mean(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

mean_list = []
for i in range(0,100):
    set_of_means= random_set_of_mean(30)
    mean_list.append(set_of_means)
    show_fig(mean_list)

std_deviation = st.stdev(mean_list)
mean = st.mean(mean_list)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

df1 = pd.read_csv("sample_2.csv")
data1 = df1["reading_time"].tolist()

sample2Mean = st.mean(data1)

fig = ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1.4], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[sample2Mean, sample2Mean], y=[0, 1.4], mode="lines", name="Mean Of The Reading Time For The Medium Articles"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 1.4], mode="lines", name="Standard Deviation 1 End"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 1.4], mode="lines", name="Standard Deviation 2 End"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 1.4], mode="lines", name="Standard Deviation 3 End"))
fig.show()

z_score = (mean - sample2Mean)/std_deviation

print("The mean of the sample mean set:", mean)
print("The standard deviation of the sameple mean set:", std_deviation)
print("The mean of sample 2:", sample2Mean)
print("The z score is:", z_score)