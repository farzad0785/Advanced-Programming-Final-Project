#Name: Aliasghar Rashidabadi
#Course: Advanced Programming
#Student ID: 40419533

"""
Please pay attention to the written comments. Most logics and syntaxes of the program is answered within them.
also in the end of the program, there are several comment, which are answers to the question in the homework file.
I appreciate for your attention.
"""

class BankAccount(object):
    def __init__(self, account_holder):
        self.name = account_holder
        self.__balance = 0
        self._transaction_history = []

        #This flag is for the user's last action. if their last action before exiting was transaction_history(), in the
        #end the program won't show them the transaction_history() output. if it wasn't, it shows the output.
        self.transaction_flag = True

    def deposit(self, amount):
        #Check for a valid amount to deposit
        if amount <= 0:
            message = "Insufficient fund. Cannot deposit 0 or negative amount. "
        else:
            self.__balance += amount
            message = f"Deposited ${amount}"
        #Recording the transaction with user info
        self._transaction_history.append(f"User: {self.name} | " + message)
        self.transaction_flag = True
        print(message)


    def withdraw(self, amount):
        #Check for a valid amount to withdraw
        if amount <= 0:
            message = "Insufficient fund. Cannot withdraw 0 or negative amount. "
        elif amount > self.__balance:
            message = "Insufficient fund. Withdrawal amount cannot be more than balance. "
        else:
            self.__balance -= amount
            message = f"Withdrew ${amount}"
        #Recording the transaction with user info
        self._transaction_history.append(f"User: {self.name} | " + message)
        self.transaction_flag = True
        print(message)

    def check_balance(self):
        #Printing the balance and recording it
        message = f"Balance checked ${self.__balance}"
        self._transaction_history.append(f"User: {self.name} | " + message)
        self.transaction_flag = True
        print(message)

    def show_history(self):
        #Print the transaction history with using separators.
        print("\n-----TRANSACTION HISTORY-----")
        for i in self._transaction_history:
            print(i)
        print("-----------------")
        self.transaction_flag = False


#----MAIN SCOPE----

try:
    #1. Program will run with the test cases in the homework file.
    #2. You, as the user, enter the inputs your self.
    test_case = int(input("Enter: \n1.Continue with system inputs \n2.Enter your desired inputs. \n"))
    while  1 > test_case or test_case > 2:
        print("Invalid input. Enter 1 or 2. Try Again.")
        test_case = int(input("Enter: \n1.Continue with system parameters \n2.Enter your desired parameters. \n"))
except:
    raise TypeError("Enter a number")
if test_case == 1:

    # Create account
    account = BankAccount("John")
    # Test all methods
    account.check_balance()  # Balance: $0
    account.deposit(100)  # Deposited $100
    account.withdraw(30) # Withdrew $30
    account.withdraw(100) # Insufficient funds!
    account.check_balance() # Balance: $70
    account.show_history()  # Show all transactions

    #Exit() to prevent running the rest of the program
    exit()

user_account = input("Enter name of the account holder: ")
bank_account = BankAccount(user_account)


#A loop in which program works until user's input is exit.
while True:
    #Valid input check
    try:
        user_choice = int(input("Enter:  1.deposit \n\t\t2.withdraw \n\t\t3.check balance"
                                " \n\t\t4.show history \n\t\t5.exit. \n"))

        while 1 > user_choice or user_choice > 5:
            print("Invalid input. Input must be a number between 1 and 5. Try again.")
            user_choice = int(input("Enter:  1.deposit \n\t\t2.withdraw \n\t\t3.check balance"
                                    " \n\t\t4.show history \n\t\t5.exit. \n"))
    except:
        raise TypeError("Invalid input. Input must be a number")

    #Transaction based on the user input
    match user_choice:
        case 1:
            user_amount = float(input("Enter the amount: "))
            bank_account.deposit(user_amount)
        case 2:
            user_amount = float(input("Enter the amount: "))
            bank_account.withdraw(user_amount)
        case 3:
            bank_account.check_balance()
        case 4:
            bank_account.show_history()
        case 5:
            print("Exiting.")
            break

#Shows the transaction history if user choose to exit before checking it
if bank_account.transaction_flag:
    bank_account.show_history()


#=====ANSWERS=====
"""
1. Try to access __balance directly from outside the class. What happens? Why? 
Answer: 
Direct access to the "__balance" instance isn't possible and appropriate. because it is set as an private
instance so it won't be accessible outside of the class.

2. Try to modify account_holder from outside. Is it possible? Should it be?
Answer:
It is possible to modify it from outside. But it is better not to be this way. Because the account_holder can be changed 
and it will make the program risky to use. It will also delete the transaction history of the previous user without saving it.

3. Create a subclass SavingsAccount that inherits from BankAccount. Can it 
access _transaction_history? Can it access __balance?
Answer:

class SavingAccount(BankAccount):
    def show_transaction(self):
        print(self._transaction_history)
    def accessing_balance(self):
        print(self.__balance) 

test = SavingAccount(bank_account) #Creating an object
test.show_transaction() #Runs perfectly fine. because the transaction_history instance is defined protected. 
test.accessing_balance() #Errors. Because balance instance is defined private. so it is not accessible outside of the class
                         #and even subclasses
                         
4. Add a property decorator (@property) for balance that allows reading but not 
setting (read-only).
Answer:
we define this block of code in the BankAccount(object) class:

    @property
    def balance(self):
        return self.__balance
"""