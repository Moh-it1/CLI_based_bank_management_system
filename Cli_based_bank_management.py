class Account:
    def __init__(self, owner_name, initial_balance):
        self.__owner_name = owner_name  
        self.__balance = initial_balance
        self.__transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Deposited {amount}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                self.__transactions.append(f"Withdrew {amount}")
            else:
                print("Insufficient balance")
        else:
            print("Invalid amount")

    def check_balance(self):
        return self.__balance
    
    def get_transaction_history(self):
        return self.__transactions
    
    def get_owner_name(self):
        return self.__owner_name


class Savingacc(Account):
    def __init__(self, owner_name, initial_balance, interest_rate):
        super().__init__(owner_name, initial_balance)
        self.__interest_rate = interest_rate

    def add_interest(self):
        interest = self.check_balance() * self.__interest_rate / 100
        self.deposit(interest)


class CurrentAcc(Account):
    def __init__(self, owner_name, initial_balance, overdraft_limit):
        super().__init__(owner_name, initial_balance)
        self.__overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > 0:
            if self.check_balance() - amount >= -self.__overdraft_limit:
                super().withdraw(amount)
            else:
                print("Exceeds overdraft limit")
        else:
            print("Invalid amount")


class Bank:
    def __init__(self):
        self.__accounts = {}

    def create_account(self, owner_name, initial_balance, account_type, extra):
        acc_number = "ACC" + str(1000 + len(self.__accounts))

        if account_type.lower() == "savings":
            account = Savingacc(owner_name, initial_balance, extra)
        elif account_type.lower() == "current":
            account = CurrentAcc(owner_name, initial_balance, extra)
        else:
            print("Invalid account type")
            return

        self.__accounts[acc_number] = account
        print(f"Account created: {acc_number}")

    def find_account(self, account_number):
        return self.__accounts.get(account_number, None)


    def save_to_file(self):
        with open("bank_data.txt", "w") as f:
            for acc_number, account in self.__accounts.items():
                owner = account.get_owner_name()
                balance = account.check_balance()
                transactions = ",".join(account.get_transaction_history())
                acc_type = "savings" if isinstance(account, Savingacc) else "current"

                line = f"{acc_number}|{owner}|{balance}|{acc_type}|{transactions}\n"
                f.write(line)


    def load_from_file(self):
        try:
            with open("bank_data.txt", "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) < 5:
                        continue

                    acc_number, owner, balance, acc_type, transactions = parts
                    balance = float(balance)

                    if acc_type == "savings":
                        account = Savingacc(owner, balance, 4)
                    else:
                        account = CurrentAcc(owner, balance, 5000)

                    if transactions:
                        account._Account__transactions = transactions.split(",")

                    self.__accounts[acc_number] = account

        except FileNotFoundError:
            pass


def main():
    bank = Bank()
    bank.load_from_file()

    while True:
        print("""
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. View Transaction History
6. Exit
""")

        choice = input("Enter Choice: ")

        if choice == "1":
            name = input("Enter name: ")
            balance = int(input("Enter initial balance: "))
            acc_type = input("Enter type (savings/current): ")
            extra = float(input("Enter interest rate or overdraft limit: "))
            bank.create_account(name, balance, acc_type, extra)

        elif choice == "2":
            acc_number = input("Enter account number: ")
            amount = int(input("Enter amount: "))
            account = bank.find_account(acc_number)
            if account:
                account.deposit(amount)
            else:
                print("Account not found")

        elif choice == "3":
            acc_number = input("Enter account number: ")
            amount = int(input("Enter amount: "))
            account = bank.find_account(acc_number)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found")

        elif choice == "4":
            acc_number = input("Enter account number: ")
            account = bank.find_account(acc_number)
            if account:
                print("Balance:", account.check_balance())
            else:
                print("Account not found")

        elif choice == "5":
            acc_number = input("Enter account number: ")
            account = bank.find_account(acc_number)
            if account:
                print("History:", account.get_transaction_history())
            else:
                print("Account not found")

        elif choice == "6":
            bank.save_to_file()
            print("Goodbye!")
            break


main()