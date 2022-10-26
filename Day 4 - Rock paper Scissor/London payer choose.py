import random
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
chs=random.randint(0,len(names)-1)
result=names[chs]
print(f"{result} is going to buy the meal today!")

print(f"my second guess will be {random.choice(names)} to buy the meal today!")
