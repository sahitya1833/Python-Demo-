class Account:
    def __init__(self):
        self.__number = 0
        self.__account_type =''
        self.__balance = 0

    def set_number(self,number):
        self.__number = number
    def get_number(self):
        return self.__number

    def set_account_type(self,type):
        self.__account_type =type
    def get_account_type(self):
        return self.__account_type

    def set_balance(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance

    def deposit(self,amt):
        self.__balance = self.__balance + amt
        print("total balance after deposit is :-",self.__balance)

    def withdrawal(self,amt):
        if amt<=self.__balance:
            self.__balance = self.__balance - amt
            print("available balance after withdrawal",self.__balance)
        else:
            print("inffusent balance...")

acc =Account()
acc.set_number(123456789)
acc.set_account_type("savings")
acc.set_balance(200)

print("account number of the user are", acc.get_number())
print("account type of the user are",acc.get_account_type())
print("user current balance",acc.get_balance())

acc.deposit(500)
acc.withdrawal(1000)

