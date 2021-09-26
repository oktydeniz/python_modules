from time import sleep


class Customer(object):
    def __init__(self, name: str, last_name: str, id_number: str, password: str):
        self.__name = name
        self.__last_name = last_name
        self.__id_number = id_number
        self.__password = password
        self.__total_money = 0

    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__last_name

    def get_id_number(self):
        return self.__id_number

    def get_password(self):
        return self.__password

    def get_total_money(self):
        return self.__total_money

    def set_total_money(self, m: int):
        self.__total_money = m


class Bank(object):
    def __init__(self, name: str):
        self.__name = name
        self.__customers = list()

    def is_customer(self, is_number: str, password: str):
        for _ in self.__customers:
            if _.get_id_number == is_number and _.get_password() == password:
                return _
        return False

    def is_buyer(self, id_no: str):
        for _ in self.__customers:
            if _.get_id_number == id_no:
                return _
        return False

    def send_money(self, sender: Customer, receiver: Customer, amount: int):
        if sender in self.__customers and receiver in self.__customers:
            if sender.get_total_money() >= amount:
                sender.set_total_money(sender.get_total_money() - amount)
                sleep(1)
                receiver.set_total_money(receiver.get_total_money() + amount)
                print("Done !")
            else:
                print("You Don't have enough money to send")
        else:
            print("Unknown Customer ")

    def be_customer(self, name: str, last_name: str, id_number: str, password: str):
        self.__customers.append(Customer(name, last_name, id_number, password))

    def take_money(self, customer: Customer, amount: int):
        if amount % 10 != 0:
            print("Only 10 and Multiples by 10")
        else:
            if customer.get_total_money() >= amount:
                print("Take your money")
                customer.set_total_money(customer.get_total_money() - amount)
            else:
                print("You Don't have enough money ")

    def add_money(self, customer: Customer, amount: int):
        if amount % 5 != 0:
            print("Only 5 and Multiples by 10")
        else:
            customer.set_total_money(customer.get_total_money() + amount)
            print("Progress Done")

    def customer_info(self, customer: Customer):
        print("""
        Name > {}
        Last Name > {}
        Amount > {}
        """.format(customer.get_name(), customer.get_last_name(), customer.get_total_money()))
