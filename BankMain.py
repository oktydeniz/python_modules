import Bank
from time import sleep


def main():
    bank = Bank.Bank("---- Bank")
    while 1:
        print("""
        [1] > New Customer
        [2] > Sing in 
        [Q,q] > Exit
        """)
        choose = input("Your Choose : ")
        if choose == "1":
            name = input("Name : ")
            last_name = input(" Last Name : ")
            id_number = input("Id Number : ")
            password = input("Password : ")
            bank.be_customer(name, last_name, id_number, password)
            input("Press Enter To Back Main Menu")
        elif choose == "Q" or choose == "q":
            print("Exiting")
            sleep(1)
            break
        elif choose == "2":
            id_no = input(" Id Number : ")
            password = input("Password : ")
            if bank.is_customer(id_no, password):
                customer = bank.is_customer(id_no, password)
                while True:
                    print("""
                    [1] > Show Info
                    [2] > Add Money
                    [3] > Take Money
                    [4] > Send Money
                    [Q] > Quit
                    """)
                    choose_customer = input("Choose  : ")
                    if choose_customer == "1":
                        bank.customer_info(customer)
                        input("Press Enter To Back Main Menu")
                    elif choose_customer == "2":
                        amount = int(input("Money : "))
                        bank.add_money(customer, amount)
                        input("Press Enter To Back Main Menu")
                    elif choose_customer == "3":
                        amount = int(input(" Money : "))
                        bank.take_money(customer, amount)
                        input("Press Enter To Back Main Menu")
                    elif choose_customer == "q" or choose_customer == "Q":
                        sleep(1)
                        break
                    elif choose_customer == "4":
                        receiver = input("Receiver Id : ")
                        amount = int(input("Amount : "))
                        if bank.is_buyer(receiver):
                            bank.send_money(customer,bank.is_buyer(receiver), amount)
                    else:
                        print(" ?? Try Again ??")
                        input("Press Enter To Back Main Menu")

            else:
                print("Unknown Customer ")
