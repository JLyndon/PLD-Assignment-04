def user_inputs():
    while True:
        usr_balance = input("Enter your balance: ")
        cost = input("\nEnter the price of an apple: ")
        if usr_balance.isdigit() and cost.isdigit() == True:
            return usr_balance, cost
        elif usr_balance.isdigit() or cost.isdigit() == True:
            if usr_balance.isdigit() == False:
                print("\nYour balance should be in numerical form.\n")
            else:
                print("\nThe rpice of an apple should be in numerical form.\n")
        else:
            print("\nPlease enter only numerical inputs.\n")

fnl_output = user_inputs()

print(fnl_output)