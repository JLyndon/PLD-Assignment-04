def user_details():
    usr_name = input("\nEnter your name: ")
    usr_age = input("Enter age: ")
    usr_address = input("Enter your address: ") 
    return usr_name, usr_age, usr_address

name, age, addr = user_details()
print(f"\nHi, my name is {name}. I am {age} years old and I live in {addr}.")