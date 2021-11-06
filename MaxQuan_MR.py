import math

def user_money():
    usr_balance = float(input("Enter your balance: "))
    return usr_balance

def apl_price():
    cost = float(input("\nEnter the price of an apple: "))
    return cost

def general_operator(balance, price):
    max_no_apl = math.floor(balance/price) 
    change = balance % price
    return max_no_apl, change

fnl_output = general_operator(user_money(), apl_price())

print(f"\nYou can buy {fnl_output[0]} apples and your change is {fnl_output[1]:.2f} pesos.")