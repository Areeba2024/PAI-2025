class Account:
    def __init__(self):
        self.__account_no = None
        self.__account_bal = None
        self.__security_code = None

    def set_data(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code

    def display_data(self):
        print("Account Details:")
        print(f"Account Number: {self.__account_no}")
        print(f"Account Balance: ${self.__account_bal}")
        print(f"Security Code: {self.__security_code}")



acc = Account()
acc.set_data("123456289", 5000.75, "AB12C3")
acc.display_data()
