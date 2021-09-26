import os
import time

online_user = False
clear = ("cls" if os.name == "nt" else "clear")


def sing_in():
    global online_user
    user_name = input("User Name : ")
    password = input("password : ")
    file = open("chat_text.txt")
    lines = file.readlines()
    online_user = False
    for user in lines:
        split = user.split()
        split_user_name = split[0]
        split_user_password = split[1]
        if split_user_name == user_name and password == split_user_password:
            online_user = user_name
    if online_user:
        print("Welcome ' " + user_name)

    else:
        print("Try Again")
    input("Press Any Key to continue")


def sing_up():
    user_name = input("User Name : ")
    mail = input("User Mail : ")
    if not control(user_name):
        print("User name already exists")
        time.sleep(1)
        os.system(clear)
        return sing_up()
    password = input("Password  : ")
    password_confirmed = input("Password Again  : ")

    if password != password_confirmed:
        print("Try Again")
        time.sleep(1)
        os.system(clear)
        return sing_up()
    file = open("chat_text.txt", "a")
    file.write(user_name)
    file.write(" ")
    file.write(password)
    file.write(" ")
    file.write(mail)
    file.write("\n")
    file.close()
    print("User saved")
    input("Press Any Key to continue")


def control(user_name):
    try:
        if user_name not in open("chat_text.text", "r").read():
            return True
        else:
            return False

    except FileNotFoundError:
        return True


if __name__ == '__main__':
    while 1:
        os.system(clear)
        print("""
        [1] Sing Up
        [2] Sing In
        [0] Close    
        """)
        choose = int(input("Your Choose > "))
        if choose == 1:
            sing_up()
        elif choose == 2:
            sing_in()
        else:
            print("incorrect entry")
