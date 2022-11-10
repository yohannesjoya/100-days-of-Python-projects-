##### Coffee Machine Project

# # services
menu={
    'espresso':{'water':50, 'coffee':18,'milk':0,'price':1.5},
    'latte':{'water':200,'coffee':24, 'milk':150,'price':2.5},
    'cappuccino':{'water':250,'coffee':24, 'milk':100,'price':3},
    'EthiopianBuna':{'water':150,'coffee':40,"milk":0,'price':5}
}
# #resources
resources={"waterT" : 300 ,"coffeeT" : 100 , "milkT" : 200 , 'Money':0}

# # coins
coins={"penny" :0.01,"nickel": 0.05,"quarter": 0.25,"dime":0.1 }
def resourceCheck(choice):
    """check resource shortage"""
    if resources['waterT']< menu[choice]['water']:
        print(f"there is no enough Water for {choice}")
        exit()
    else:
       if resources['coffeeT']<menu[choice]['coffee']:
           print(f"there is no enough coffee for {choice}")
           exit()
       else:
           if resources['milkT']<menu[choice]['milk']:
               print(f"there is no enough milk for {choice}")
               exit()
           else:
               return True

def Transaction(choice):
    """process coins and process kitchen work"""
    print('Please insert Coins.')
    paymentQuarters = float(input("How many Quarter?: ")) 
    paymentDimes = float(input("How many Dime?: ")) 
    paymentNickels = float(input("How many Nickels?: "))
    paymentPennies = float(input("How many Pennies?: "))
    TotalPayment = (coins['penny']*paymentPennies)+(coins['quarter']*paymentQuarters)+(coins['dime']*paymentDimes)+(coins['nickel']*paymentNickels)
    if TotalPayment>= menu[choice]['price']:
        change = TotalPayment-menu[choice]['price']
        resources['Money']+=menu[choice]['price']
        
        resources['waterT']-=menu[choice]['water']
        resources['milkT']-= menu[choice]['milk']
        resources['coffeeT']-=menu[choice]['coffee']
        
        print(f'Here is {change} in change.')
        print(f'Here is your {choice} Enjoy')
        print()#space holders
        print()#space holders
        
    else:
        print(f"you dont have enough money to buy {choice} \n:your money is ${TotalPayment}: and \nthe price of {choice} is ${menu[FinalChoice]['price']}")


def calculateServe(choice):
    """checks the correctness of choice and calculate coins finally serves"""
    # FinalChoice=seym(choice)
    FinalChoice=choice
    if (choice!='espresso') and (choice!='latte') and(choice!='cappuccino') and (choice!='EthiopianBuna'):
       print("We Dont Give This Service")
       again = input('\nDo You Want to Try Again? YES or NO\n').lower()
       if again=='yes':
           coffee()
       else:
           print('Thanks for your time')
           exit()
    
   
    if resourceCheck(FinalChoice):
        Transaction(FinalChoice)
        

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



