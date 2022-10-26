# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
fullname=(name1+name2).lower()
count1=fullname.count("t")+fullname.count("r")+fullname.count("u")+fullname.count("e")
count2=fullname.count("l")+fullname.count("o")+fullname.count("v")+fullname.count("e")
score=str(count1)+str(count2)
result=int(score)

if result<10 or result>90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result>=40 and result<=50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")
