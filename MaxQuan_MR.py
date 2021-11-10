import math 

def user_inputs():
    while True:
        usr_balance = input("Enter your balance: ")
        cost = input("\nEnter the price of an apple: ")
        if usr_balance.isdigit() and cost.isdigit() == True:
            money = float(usr_balance)
            price = float(cost)
            return money, price
        elif usr_balance.isspace() or cost.isspace() == True:
            print("Please fill all the blanks.")
        elif usr_balance.isalpha() and cost.isalpha() == True:
                print("Inputs should be in numerical form.")
        elif (usr_balance.isalpha() and cost.isalpha() == True) == False:
            if usr_balance.isalpha() == True:
                print("Your balance should be in numerical form.")
            elif cost.isalpha() == True:
                print("The price should be in numerical form.")           

def general_operator(balance, price):
    max_no_apl = math.floor(balance/price) 
    change = balance % price
    return max_no_apl, change

dividend, divisor = user_inputs()

fnl_output1, fnl_output2 = general_operator(dividend, divisor)

print(f"\nYou can buy {fnl_output1} apples and your change is {fnl_output2:.2f} pesos.")