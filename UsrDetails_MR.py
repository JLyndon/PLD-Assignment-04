def user_deets():
    usr_name = input("\nEnter your name: ")
    usr_age = input("Enter age: ")
    usr_address = input("Enter your address: ") 
    return usr_name, usr_age, usr_address

user_info = user_deets()
print(f"\nHi, my name is {user_info[0]}. I am {user_info[1]} years old and I live in {user_info[2]}.")