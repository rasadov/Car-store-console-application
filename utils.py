from classes import User
import database
import pandas as pd


def buy():
    database.show_cars()
    enter = input("which car you wanna buy? ")
    database.show_car(enter)


def sell(user: User):
    producer = input("Enter the producer of the car: ")
    model = input("Enter the model of the car: ")
    type = input("Enter the type of the car (sedan, suv, sportcar,...): ")
    year = input("Enter the year of production of the car: ")
    hp = input("Enter the hp of the car: ")
    cap = input("Enter the engine capacity of the car: ")
    color = input("Enter the color of the car: ")
    a = user.__str__()
    database.add(producer, model, type, year, hp, cap, color, a)


def check_user():
    enter = input("log in or register? ")
    if enter == "exit":
        return "exit"
    elif enter == "log in":
        # global user
        user = input("Enter username ")
        password = input("Enter password ")
        ans = database.login(user, password)
        if (ans == 0):
            print("Incorrect username or password")
            user = 0
            return False

    elif enter == "register":
        # global user
        user = input("Create a username: ")
        if database.username_exist(user) == False:
            passwordofuser = input("Create a password: ")
            while len(passwordofuser) < 8:
                passwordofuser = input("It should be 8 characters minimum: ")
            nameofuser = input("Enter name ")
            surnameofuser = input("Enter surname ")
            bdofuser = input("Enter birthday ")
            database.register(user, nameofuser, surnameofuser,
                              bdofuser, passwordofuser)
            print("New account registrated")
            user = 0
            return False
        else:
            print("This username is already taken")
            user = 0
            return False
    elif enter == "exit":
        return "exit"
    else:
        print("No such command")
        return "exit"

    if type(user) != str:
        return False
    if database.username_exist(user) != True:
        print("first you have to log in")
        user = 0
        return False
    return database.userclass(user)


def customer(enter, user: User):
    if enter == "buy":
        database.show_cars()
        enter = input("which car you wanna buy? ")
        database.show_car(enter)

    elif enter == "card":
        enter = input("show/add/remove? ")
        if enter == "show":
            database.show_card(user)
        elif enter == "add":
            database.show_cars()
            enter = input("which car? ")
            database.add_to_card(user, int(enter))
        elif enter == "remove":
            database.show_card()
            enter = input("which car? ")
            database.remove_from_card(user, int(enter))

    elif enter == "sell":
        producer = input("Enter the producer of the car: ")
        model = input("Enter the model of the car: ")
        type = input("Enter the type of the car (sedan, suv, sportcar,...): ")
        year = input("Enter the year of production of the car: ")
        hp = input("Enter the hp of the car: ")
        cap = input("Enter the engine capacity of the car: ")
        color = input("Enter the color of the car: ")
        database.add(producer, model, type, year, hp, cap, color, user)

    elif enter == "my account":
        database.dashboard(user)
        enter = input("change account/car or skip ")
        if enter == "skip":
            pass
        elif enter == "account":
            enter = input("What do you want to change? ")
            if enter == "name":
                user.name = input("New name: ")
            elif enter == "surname":
                user.surname = input("New surname: ")
            elif enter == "birthday":
                user.birthday = input("New birthday: ")
            elif enter == "password":
                password = input("your previous password: ")
                if password == user.password:
                    user.password = input("New passwod: ")
            else:
                print("No such command")
        elif enter == "car":
            df = pd.read_csv("database.csv")
            id = int(input("which car you wanna change? "))
            if id == "exit" or id >= len(df):
                return
            if df.loc[id, "owner"] == user.username:
                enter = input("What column do you want to change? ")
                df.loc[id, enter] = input("New value: ")
                df.to_csv("database.csv", index=False, sep=',')
            else:
                print("It's not your car")

        else:
            print("No such command")

    elif enter == "exit":
        return "exit"

    else:
        print("No such command")


def admin(enter, user: User):
    if enter == "card":
        enter = input("show/add/remove? ")
        if enter == "show":
            database.show_card(user)
        elif enter == "add":
            database.show_cars()
            enter = input("which car? ")
            database.add_to_card(user, int(enter))
        elif enter == "remove":
            database.show_card()
            enter = input("which car? ")
            database.remove_from_card(user, int(enter))

    elif enter == "buy":
        database.show_cars()
        enter = input("buy/add to card? ")
        if enter == "buy":
            enter = input("which car? ")
            database.show_car(enter)

    elif enter == "sell":
        producer = input("Enter the producer of the car: ")
        model = input("Enter the model of the car: ")
        type = input("Enter the type of the car (sedan, suv, sportcar,...): ")
        year = input("Enter the year of production of the car: ")
        hp = input("Enter the hp of the car: ")
        cap = input("Enter the engine capacity of the car: ")
        color = input("Enter the color of the car: ")
        database.add(producer, model, type, year, hp, cap, color, user)

    elif enter == "my account":
        df = database.dashboard(user)
        enter = input("change account/car or skip ")
        if enter == "skip":
            pass
        elif enter == "account":
            enter = input("What do you want to change? ")
            if enter == "name":
                user.name = input("New name: ")
            elif enter == "surname":
                user.surname = input("New surname: ")
            elif enter == "birthday":
                user.birthday = input("New birthday: ")
            elif enter == "password":
                password = input("your previous password: ")
                if password == user.password:
                    user.password = input("New passwod: ")
            else:
                print("No such command")
        elif enter == "car":
            df = pd.read_csv("database.csv")
            id = int(input("which car you wanna change? "))
            if id == "exit" or id >= len(df):
                return
            if df.loc[id, "owner"] == user.username:
                enter = input("What column do you want to change? ")
                df.loc[id, enter] = input("New value: ")
                df.to_csv("database.csv", index=False, sep=',')
            else:
                print("Error")

    elif enter == "log out":
        user = 0

    elif enter == "database":
        print("In order to leave this page enter '0' ")
        while (enter != '0'):
            enter = input("Users or cars: ")
            if enter == "users":
                df = pd.read_csv('users.csv')
                print(df)
                enter = input("remove/skip: ")
                if enter == "skip":
                    pass
                elif enter == "remove":
                    ind = int(input("which item to remove? "))
                    database.remove_user(ind - 1, "users.csv", "database.csv")

            if enter == "cars":
                df = pd.read_csv('database.csv')
                print(df)
                enter = input("remove/edit/skip: ")
                if enter == "skip":
                    pass
                elif enter == "remove":
                    ind = int(input("which item to remove? "))
                    database.remove_car(ind - 1, "database.csv")
                elif enter == "edit":
                    df = pd.read_csv("database.csv")
                    print(df)
                    id = int(input("which car you wanna change? "))
                    if id == "exit" or id >= len(df):
                        return
                    enter = input("What column do you want to change? ")
                    df.loc[id, enter] = input("New value: ")
                    df.to_csv("database.csv", index=False, sep=',')

    else:
        print("No such command")


if __name__ == "__main__":
    pass
