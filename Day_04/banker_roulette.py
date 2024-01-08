import random

names_string = input('Enter names of people: \n')
names = names_string.split(", ")

choice = random.randint(0, len(names)-1)
paid_by = names[choice]
print(f"{paid_by} is going to buy the meal today!")
