import math 

def user_inputs():
    while True:
        usr_balance = input("\nEnter your balance: ")
        cost = input("\nEnter the price of an apple: ")
        if usr_balance.isdigit() and cost.isdigit() == True:
            return usr_balance, cost
        elif usr_balance.isspace() or cost.isspace() == True:
            print("Please fill all the blanks.")
        elif usr_balance.isalpha() and cost.isalpha() == True:
                print("Inputs should be in numerical form.")
        elif usr_balance.isalpha() or cost.isalpha() == True:
            if usr_balance.isalpha() == True:
                print("Your balance should be in numerical form.")
            elif cost.isalpha() == True:
                print("The price should be in numerical form.")
        else:
            if "," in usr_balance or cost == True:
                DC_Balance, DC_Cost = CommaReader_Gen(usr_balance, cost)
                if DC_Balance.replace(".","").isdigit() and DC_Cost.replace(".","").isdigit() == True:
                    return DC_Balance, DC_Cost

def CommaReader_Gen(Num01, Num02):
    if "," in Num01 and Num02:
        Bal_01 = Num01.replace(",","")
        Cost_02 = Num02.replace(",","")
        return Bal_01, Cost_02
    elif "," in Num01:
        BalanceOnly = Num01.replace(",","")
        return BalanceOnly, Num02
    elif "," in Num02:
        CostOnly = Num02.replace(",","")
        return Num01, CostOnly
    else:
        return Num01, Num02                

def general_operator(balance, price):
    dvnd = float(balance)
    dvsr = float(price)
    max_no_apl = math.floor(dvnd/dvsr) 
    change = dvnd % dvsr
    return max_no_apl, change

dividend, divisor = user_inputs()

fnl_output1, fnl_output2 = general_operator(dividend, divisor)

print(f"\nYou can buy {fnl_output1} apples and your change is {fnl_output2:.2f} pesos.")