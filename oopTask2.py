import csv
import os


class Dollars:
    def __get__(self, instance, owner):
        return instance.__dict__["_list_dollar"]

    def __set__(self, instance, value):
        instance.__dict__["_list_dollar"] = value


class UserPortfolio:
    _list_dollar = Dollars()

    def __init__(self, name):
        self._name = name
        self._list_crypto = {}
        self._list_dollar = {}

    def __str__(self):
        return self._name


class Portfolios:
    __list_name = []

    def __init__(self):
        self._new_list_client = []
        self.__list_client = []

    def create_portfolio(self, name):
        self.__list_name.append(name)
        client = UserPortfolio(name)
        self.__list_client.append(client)
        self.show()
        print("Portfolio created\n")

    def add_cryptocurrencies(self, name):
        user = None
        for i in self.__list_client:
            if str(i) == name:
                user = i
        while True:
            try:
                print(f"\tMenu adding cryptocurrency")
                crypto = str(input("Enter cryptocurrencies: ").lower())
                price = int(input("Enter the amount of cryptocurrency: "))
                user._list_crypto[crypto] = price
                print("Cryptocurrency added\n")
                break
            except ValueError() as s:
                print("The data is entered incorrectly")

    def name_verification(self, name):
        try:
            if len(self.__list_client) == 0:
                print("! - You have not created a portfolio\n")
                self.mini_menu()
                return False
            elif name not in self.__list_name:
                print("! - You have not created a portfolio\n")
                self.mini_menu()
                return False
            else:
                return name
        except ValueError as s:
            print("Error!!! Incorrect data entered\n\n")

    def show(self):
        count = 1
        for i in self.__list_client:
            print(i.__dict__)
            print(f"User - {count}")
            print(f"Name - {i._name.title()}\n"
                  f"Cryptocurrencies - {i._list_crypto}\n"
                  f"Crypto in dollar - {i._list_dollar}$")
            print()
            count += 1

    def mini_menu(self):
        while True:
            try:
                selection = input("Do you want to create a portfolio with this name?\n"
                                  "Enter 'y' if yes or 'n' if no: ")
                if selection != 'y' and selection != 'n':
                    raise ValueError()
                elif selection == 'y':
                    name = input("Enter the new name: ")
                    if 1 >= len(name) > 20:
                        raise ValueError()
                    self.create_portfolio(name)
                    return False
                elif selection == 'n':
                    return False
            except ValueError as s:
                print("Error!!! Enter 'y' or 'n'\n")

    def delete_cryptocurrencies(self, name: str, cripta: str):
        print("\tRemove cryptocurrencies")
        try:
            for user in self.__list_client:
                if name == str(user):
                    print(str(user))
                    print(type(cripta))
                    user._list_crypto.pop(cripta, "key not found")
                    user._list_dollar.pop(cripta, '')
                    print("The operation was successful\n\n")

        except ValueError as s:
            print("Error!!! Incorrect data entered\n")

    def convert_cryptocurrencies(self, name):
        for user in self.__list_client:
            if name == str(user):
                for key, value in user._list_crypto.items():
                    user._list_dollar[key] = value * 40

    def sort_portfolio(self, name):
        for i in self.__list_client:
            if name == str(i):
                i._list_dollar = dict(sorted(i._list_dollar.items(),
                                             key=lambda item: item[1]))
                i._list_crypto = dict(sorted(i._list_crypto.items(),
                                             key=lambda item: item[1]))

    def save_portfolio(self, name, file_name: str):
        if not file_name.endswith('.csv'):
            file_name = file_name + '.csv'
        user = None
        for i in self.__list_client:
            if name == str(i):
                user = i
        header = ["Name", "List cripto", "List dollar"]
        with open(file_name, "w", newline='') as file:
            dict_writer = csv.DictWriter(file, fieldnames=header)
            dict_writer.writeheader()
            for i in self.__list_client:
                info = {"Name": i._name.title(), "List cripto": i._list_crypto, "List dollar": i._list_dollar}
                dict_writer.writerow(info)

    def init_portfolio(self, file_name):
        with open(file_name, "r", newline='') as file:
            dict_reader = csv.DictReader(file)
            for portfolio in dict_reader:
                print(portfolio)
                new_obj = None
                for key, value in portfolio.items():
                    if key == 'Name':
                        new_obj = UserPortfolio(value)
                    if key == "List cripto":
                        new_obj._list_crypto = value
                    if key == "List dollar":
                        new_obj._list_dollar = value
                self._new_list_client.append(new_obj)

        count = 1
        for i in self._new_list_client:
            print(f"User - {count}")
            print(f"Name - {i._name.title()}\n"
                  f"Cryptocurrencies - {i._list_crypto}\n"
                  f"Crypto in dollar - {i._list_dollar}$")
            print()
            count += 1

    def menu(self):
        while True:
            print(f"\tMenu Portfolios")
            print(f"1.Create a portfolio\n"
                  f"2.Add Cryptocurrencies\n"
                  f"3.Remove cryptocurrencies\n"
                  f"4.Convert cryptocurrency to dollars\n"
                  f"5.Show info portfolio\n"
                  f"6.Sort the portfolio\n"
                  f"7.Save portfolio data file\n"
                  f"8.Download portfolio data from the file\n"
                  f"9.Exit")
            try:
                choice = int(input("Enter the selection: "))
                print()
                if choice == 1:
                    try:
                        print("\tCreate a portfolio")
                        name = input("Enter a name for the new portfolio: ").lower()
                        print()
                        if 1 >= len(name) > 30:
                            raise ValueError()
                        self.create_portfolio(name)
                    except ValueError as s:
                        print("The name is not correct")
                elif choice == 2:
                    name = input("Enter a portfolio name to add currency: ").lower()
                    vertif = self.name_verification(name)
                    if vertif:
                        self.add_cryptocurrencies(vertif)
                elif choice == 3:
                    try:
                        user = input("Enter the name user portfolio: ").lower()
                        name_cripto = str(input("Enter the cryptocurrency you want to delete: ")).lower()
                        print(name_cripto)
                        if user not in self.__list_name:
                            print("Error!!! Name not found\n")
                        else:
                            self.delete_cryptocurrencies(user, name_cripto)
                    except ValueError as s:
                        print("Error!!! The name is not correct\n")
                elif choice == 4:
                    try:
                        name = input("Enter the name: ").lower()
                        print()
                        if 1 >= len(name) > 20:
                            raise ValueError()
                        self.convert_cryptocurrencies(name)
                    except ValueError as s:
                        print("Error!!! The name is not correct\n")
                elif choice == 5:
                    self.show()
                elif choice == 6:
                    name = input("Enter a name portfolio sort: ").lower()
                    res = self.name_verification(name)
                    self.sort_portfolio(name)
                elif choice == 7:
                    name = input("Enter a name portfolio if save: ").lower()
                    vertif = self.name_verification(name)
                    if vertif:
                        file_name = str(input("Enter the name file: "))
                        self.save_portfolio(vertif, file_name)

                elif choice == 8:
                    file_name = str(input("Enter the name file: "))
                    if not file_name.endswith('.csv'):
                        file_name = file_name + '.csv'
                    elif file_name not in os.listdir():
                        raise FileNotFoundError(f"This file does not exist")
                    self.init_portfolio(file_name)
                elif choice == 9:
                    print("\tExit")
                    break
                else:
                    print("I don't know such a command, enter the choice from 1 to 9")
            except ValueError as s:
                print("Error! Incorrect selection")


if __name__ == '__main__':
    portfolio = Portfolios()
    portfolio.menu()
