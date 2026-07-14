# wap to create a class called bank having properties as 
# class property - bank name and brach and having object property
# as bank holder name ,account number and balance with methods to deposit
# withdraw and display . design to child class called saving account and 
# salary account . saving account having a method add interest to update the main 
# account balance. salary account having overwriden methods deposit with a 
# limit of 20,000 and withdraw with a minimum limit of 10,000
# note - account holder name and account number must be verified before 
# storing 
# keep balance as a private attribute and design a abstract method in the 
# parent class which will be inherited by saving account called as 
# add interest 
# constructor chaining method chaining and abstraction
# is being used in this code
# design a class method in the parent class to change the branch of 
# bank
from abc import ABC,abstractmethod
class bank(ABC):
    bank_name = "sbi"
    branch_name = "landran"
    def __init__(self,account_holder,account_number,account_balance):
        self.account_holder = self.verify_account_holder(account_holder)
        self.account_number = self.verify_account_number(account_number)
        self.__balance = account_balance
    @staticmethod
    def verify_account_number(account_number):
        if len(str(account_number))== 10 and str(account_number).isdigit():
            return account_number
        else :
            raise ValueError("account number must be 10 digit")
    @staticmethod
    def verify_account_holder(account_name):
        if account_name.replace(" ","").isalpha():
            return account_name
        else:
            raise ValueError("account number must be alphabet")
    @classmethod
    def change_branch(cls,new_branch):
        cls.branch_name = new_branch
        print(f"\All accounts migrated to the {cls.branch} branch.")
    def display_detail(self):
        print(f'Customer Name : {self.holder_name}')
        print(f'Account Type  : {self.account_type}')
        print(f'AC No         : {self.account_number}')
        print(f'Branch        : {self.branch}')
        print(f'Balance       : {self.__balance}')    
    
    def get_balance(self):
        return self.__balance

    def update_balance(self, amount):
        self.__balance += amount
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"\nSuccess: Deposited {amount}. Updated Balance: {self.__balance}")
        else:
            print("\nTransaction Failed: Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"\nSuccess: Withdrawn {amount}. Remaining Balance: {self.__balance}")
        else:
            print("\nTransaction Failed: Insufficient funds.")

    @abstractmethod
    def add_interest(self):
        pass
class SavingAccount(bank):
        def __init__(self, holder_name, account_number, balance):
            super().__init__(holder_name, account_number, balance)
            self.account_type = "Savings Account"

        def add_interest(self):
            interest = self.get_balance() * 0.05
            self.update_balance(interest)
            print(f"\nSuccess: 5% Interest Added ({interest}). New Balance: {self.get_balance()}")


class SalaryAccount(Bank):
        def __init__(self, holder_name, account_number, balance):
            super().__init__(holder_name, account_number, balance)
            self.account_type = "Salary Account"

        def add_interest(self):
            print("\nNotice: Salary Accounts do not accrue interest, Gawarooo......")

        def deposit(self, amount):
            # Restricts deposits exceeding 20,000
            if amount < 20000:
                print("\nTransaction Denied: Deposit should be more than 20,000.")
            else:
                super().deposit(amount)

        def withdraw(self, amount):
            # Restricts withdrawals exceeding 10,000
            if amount < 10000:
                print("\nTransaction Denied: Withdrawal should be more than 10,000.")
            else:
                super().withdraw(amount)


# --- Database & Operational Logic ---

bank_database = {}

def add_account():
    print("\n--- Register New Client ---")

    try:
        # The int() conversion is now safely inside the try block
        acc_type = int(input("Select Account Type (1 for Savings, 2 for Salary): "))
        name = input("Enter Account Holder Name: ")
        acc_no = input("Enter 10-Digit Account Number: ")

        # Check for duplicates before asking for money
        if acc_no in bank_database:
            print("\nSystem Error: Account number already active in the database.")
            return

        # The float() conversion is also protected
        balance = float(input("Enter Initial Deposit: "))

        # Note: acc_type is now an integer, so we check against 1 and 2 (not '1' and '2')
        if acc_type == 1:
            new_account = SavingAccount(name, acc_no, balance)
        elif acc_type == 2:
            new_account = SalaryAccount(name, acc_no, balance)
        else:
            print("\nSystem Error: Invalid account type selected. Please enter 1 or 2.")
            return

        # Store in database
        bank_database[acc_no] = new_account
        print(f"\nSuccess: {new_account.account_type} established for {name}.")

    except ValueError as e:
        # Differentiates between Python's built-in input errors and your custom Bank class errors
        if "invalid literal" in str(e) or "could not convert" in str(e):
            print("\nInput Error: A numerical value was expected, but text was provided.")
        else:
            print(f"\nValidation Error: {e}")

    except Exception as e:
        # A failsafe for any unforeseen system crashes
        print(f"\nUnexpected System Error: {e}")


# --- Primary User Interface ---

while True:
    print("\n===== BANK TERMINAL =====")
    print("1. Register New Account")
    print("2. View Account Details")
    print("3. Process Deposit")
    print("4. Process Withdrawal")
    print("5. Apply Account Interest")
    print("6. Update Branch Location")
    print("7. Terminate Session")

    try:
        choice = int(input("Select operation (1-7): "))
    except ValueError:
        print("\nInput Error: Numerical value required.")
        continue

    if choice == 1:
        add_account()

    elif choice == 6:
        new_branch_name = input("Enter the new branch designation: ")
        Bank.change_branch(new_branch_name)

    elif choice == 7:
        print("\nSession terminated. System shutting down.")
        break

    elif choice in [2, 3, 4, 5]:
        search_acc = input("Enter 10-Digit Account Number: ")

        if search_acc not in bank_database:
            print("\nLookup Failed: Account not found in current database.")
            continue

        current_account = bank_database[search_acc]

        if choice == 2:
            current_account.display_details()
        elif choice == 3:
            try:
                amt = float(input("Enter deposit amount: "))
                current_account.deposit(amt)
            except ValueError:
                print("\nInput Error: Valid monetary amount required.")
        elif choice == 4:
            try:
                amt = float(input("Enter withdrawal amount: "))
                current_account.withdraw(amt)
            except ValueError:
                print("\nInput Error: Valid monetary amount required.")
        elif choice == 5:
            current_account.add_interest()

    else:
        print("\nInvalid operation. Select a valid menu option.")