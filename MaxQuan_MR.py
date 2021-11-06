import math 

def user_inputs():
    while True:
        usr_balance = input("Enter your balance: ")
        cost = input("\nEnter the price of an apple: ")
        if usr_balance.replace(".", "", 1).isdigit() and cost.replace(".", "", 1).isdigit() == True:
            money = float(usr_balance)
            price = float(cost)
            return money, price
        elif usr_balance.replace(".", "", 1).isdigit() or cost.replace(".", "", 1).isdigit() == True:
            if usr_balance.isdigit() == False:
                print("\nYour balance should be in numerical form.\n")
            else:
                print("\nThe price of an apple should be in numerical form.\n")
        else:
            print("\nPlease enter only numerical inputs.\n")

def general_operator(balance, price):
    max_no_apl = math.floor(balance/price) 
    change = balance % price
    return max_no_apl, change

dividend, divisor = user_inputs()

fnl_output1, fnl_output2 = general_operator(dividend, divisor)

print(f"\nYou can buy {fnl_output1} apples and your change is {fnl_output2:.2f} pesos.")