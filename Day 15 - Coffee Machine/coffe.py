##### Coffee Machine Project

# # services
espresso={'water':50, 'coffee':18,'milk':0,'price':1.5}
latte = {'water':200,'coffee':24, 'milk':150,'price':2.5}
cappuccino={'water':250,'coffee':24, 'milk':100,'price':3}
EthiopianBuna={'water':150,'coffee':40,"milk":0,'price':5}

# #resources
resources={"waterT" : 300 ,"coffeeT" : 100 , "milkT" : 200 , 'Money':0}

# # coins
coins={"penny" :0.01,"nickel": 0.05,"quarter": 0.25,"dime":0.1 }

mychoice = vars()

def seym(choice):
    if choice=='latte':
        mychoice[choice]= latte
    elif choice=='espresso':
        mychoice[choice]=espresso
    elif choice=="cappuccino":
        mychoice[choice]=cappuccino
    elif choice=='EthiopianBuna':
        mychoice[choice]=EthiopianBuna
    else:
        print("Wrong choice We Dont Give This Service")
        exit()
    return mychoice[choice]
    


def calculateServe(choice):
    FinalChoice=seym(choice)
   
    
    if resources['waterT']<FinalChoice['water']:
        print(f"there is no enough Water for {choice}")
        # do this
    else:
       if resources['coffeeT']<FinalChoice['coffee']:
           print(f"there is no enough coffee for {choice}")
       else:
           if resources['milkT']<FinalChoice['milk']:
               print(f"there is no enough milk for {choice}")
           else:
               print('Please insert Coins.')
               paymentQuarters = float(input("How many Quarter?: ")) 
               paymentDimes = float(input("How many Dime?: ")) 
               paymentNickels = float(input("How many Nickels?: "))
               paymentPennies = float(input("How many Pennies?: "))
               TotalPayment = (coins['penny']*paymentPennies)+(coins['quarter']*paymentQuarters)+(coins['dime']*paymentDimes)+(coins['nickel']*paymentNickels)
               if TotalPayment>= FinalChoice['price']:
                   change = TotalPayment-FinalChoice['price']
                   resources['Money']+=FinalChoice['price']
                   
                   resources['waterT']-=FinalChoice['water']
                   resources['milkT']-= FinalChoice['milk']
                   resources['coffeeT']-=FinalChoice['coffee']
                   
                   print(f'Here is {change} in change.')
                   print(f'Here is your {choice} Enjoy')

                   
               else:
                   print(f"you dont have enough money to buy {choice} \n:your money is ${TotalPayment}: and \nthe price of {choice} is ${FinalChoice['price']}")


def coffee():
    choice = input("what would you like? (espresso/latte/cappuccino/EthiopianBuna): ")
    if choice=='report':
        print(f"Water: {resources['waterT']}ml")
        print(f"Milk: {resources['milkT']}ml")
        print(f"Coffee: {resources['coffeeT']}g")
        print(f"Money: ${resources['Money']}")
        coffee()
        
    else:
        calculateServe(choice)
        coffee()

    
    
coffee()            



