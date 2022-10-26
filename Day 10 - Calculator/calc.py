import os
def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b

operations={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}
from art import logo

def calculator():
  print(logo)

  contin_ue="y"
  firstno = float(input("What is the first number?:  "))
  for op in operations:
      print(op)
  while contin_ue=='y':
    chosenoperation=input("Pick an operation:  ")
    lastno=float(input("What is the next number?:  "))
    answer=operations[chosenoperation](firstno,lastno)
    print(f"{firstno} {chosenoperation} {lastno} = {answer}")
    contin_ue= input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
  
    if contin_ue =="n":
        os.system('cls' if os.name == 'nt' else 'clear')
        calculator()
    firstno = answer
  
calculator()
