# with open("weather_data.csv") as data:
#     weather = data.readlines()
#     for weather_report in weather:
#         stripped = weather_report.strip()
#         print(weather_report)

# import csv
#
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# total_temp = len(temp_list)

# Sum = sum(temp_list)
# average = Sum / total_temp
# print(round(average, 1))

# print(data["temp"].mean())
# max_temp = data["temp"].max()

# get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# Monday temperature in Fahrenheit

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# data_dict = {
#     "Students": ["Amy", "James", "Ayan"],
#     "Scores": [75, 65, 95]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color_count = len(data[data["Primary Fur Color"] == "Gray"])
red_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [gray_color_count, red_color_count, black_color_count]
}

Squirrel_table = pandas.DataFrame(data_dict)
Squirrel_table.to_csv("Squirrel.csv")
