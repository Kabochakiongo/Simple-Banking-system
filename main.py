

class Account():
     def __init__(self,name,id,balance):
          self.username = name
          self.account_number = id
          self.balance = balance

#including a Deposit method

     def Deposit(self,amount):
          self.balance += amount
          print(f"{self.username} Deposited {amount}$. Current balance is {self.balance}")

#including a withdrawal method

     def Withdrawal(self,amount):
          if self.balance >= amount:
               self.balance -= amount
               print(f"(self.username) Withdrew {amount}$. Current balance is {self.balance}")

          else:
               print("You don't have enough funds to Withdraw")

#including a child class to calculate the interest rate for our account

class Savings_Account(Account):
     def __init__(self,name,id,balance,interest_rate):
          super().__init__(name,id,balance)
          self.interest_rate = interest_rate

     def add_interest(self):
          interest = self.balance * self.interest_rate
          self.Deposit(interest)

# Interacting and testing the program

account1 = Account("John","1234456",1000)
account1.Deposit(500)
account1.Withdrawal(200)

print()

Savings_account = Savings_Account("Viny","6723112",2000,0.9)
Savings_account.Deposit(1000)
Savings_account.add_interest()
Savings_account.Withdrawal(500)
Savings_account.Withdrawal(1000)
Savings_account.Withdrawal(5000)

