from database import login, register, dashboard, add, username_exist, show_cars, show_car, userclass
from classes import User
from utils import main

enter = ""
user = 0

while (enter != "exit"):
    if user == 0:
        enter = input("log in or register? ")
        if enter == "log in":
            user = input("Enter username ")
            password = input("Enter password ")
            ans = login(user, password)
            if (ans == 0):
                print("No account like this was found")
                user = 0
                continue
        if enter == "register":
            user = input("Create a username: ")
            if username_exist(user) == False:
                passwordofuser = input("Create a password: ")
                while len(passwordofuser) < 8:
                    passwordofuser = input(
                        "It should be 8 characters minimum: ")
                nameofuser = input("Enter name ")
                surnameofuser = input("Enter surname ")
                bdofuser = input("Enter birthday ")
                register(user, nameofuser, surnameofuser,
                         bdofuser, passwordofuser)
                print("New account registrated")
                user = 0
                continue
            else:
                print("This username is already taken")
                user = 0
                continue
        if username_exist(user) != True:
            print("first you have to log in")
            user = 0
            continue
        else:
            print(user)
            print(user + "-----------------------")
            user = userclass(user)

    enter = input("""-Buy a car
-Sell a car
-My account
-Log out
""")
    main(enter, user)


"""
- create account:
    - admin
    - customer
- log in:
    see my dashboard
- buy cars
- sell cars

"""
