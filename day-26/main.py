import random

# for n in range(1, 5):
#     n = n * 2
#     print(n)

# new_num = [n * 2 for n in range(1, 5)]
# print(new_num)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_name = [name for name in names if len(name) < 5]
# uppercase_name = [name.upper() for name in names if len(name) > 5]
# print(uppercase_name)

# TODO: Squared Numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)

# TODO: Even Numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# TODO: List Comprehension 3
# with open("file1.txt") as file1:
#     file_one = file1.read().splitlines()
#
# with open("file2.txt") as file2:
#     file_two = file2.read().splitlines()
#
# result = [int(num) for num in file_one if num in file_two]
#
# print(result)

# DICTIONARY COMPREHENSION

# TODO: Names

names = {"Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"}

student_scores = {student: random.randint(1, 100) for student in names}

passed_students = {student: scores for(student, scores) in student_scores.items() if scores >= 60}
print(passed_students)

# TODO: Dictionary Comprehension 1
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # split() is used to loop through list of words instead of letters
# result = {word: len(word) for word in sentence.split()}
# print(result)

# TODO: Dictionary Comprehension 2

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day: temp_c*9/5 + 32 for(day, temp_c) in weather_c.items()}
# print(weather_f)


