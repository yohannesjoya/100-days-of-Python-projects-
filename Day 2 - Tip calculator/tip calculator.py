#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to tip calculator")
total=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip_percent=tip/100
no_ofPeople=int(input("How many people to split the bill? "))
total_after_tip = total+(total*tip_percent)

# the best way to round is below
each_stake ="{:.2f}".format((total_after_tip/no_ofPeople))


message=f"Each person should pay: ${each_stake}"
print(message)


