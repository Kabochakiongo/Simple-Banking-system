balance = 0


def Deposit ():
    deposit = int(input("Enter amount you would like to Deposit: "))
    userbal = 0
    if  deposit < int(50):
         print("Sorry you can't deposit money less than 50 shillings")

    elif deposit > int(500000):
         print("Sorry you can't deposit money exceding 500000")

    else:
         userbal = userbal + deposit
         print("Confirm you have succesfully deposited shillings",deposit,"to your account your new balance is shillings",userbal)
         exit()


def Withdraw():
    min_limit = userbal + transaction
    userbal = 30000
    transaction = 50
    withdraw = int(input("Enter amount you would like to Withdraw: "))
    if withdraw < min_limit:
         print("sorry you have insufficient Balance, your account balance is:",userbal)
    elif withdraw <= int(99):
         print("Sorry you can't withdraw money less than 100 shillings")
    elif withdraw >= int(300001):
         print("Sorry you can't withdraw money exceding 300000")
    else:
         userbal = userbal - int(withdraw)
         userbal = userbal - transaction
         print("Confirm you have succesfully deposited shillings",withdraw,"to your account your new balance is shillings",userbal)

         exit()


def Checkbal():
     verify = input("Please verify password to check balance: ")
     if verify == password:
          print(balance)
     else:
          print("Incorrect password")
          exit()

username = "Sam"
password ="123"

def Authencication():
        if fname == username and pwd == password:
             print("Welcome back",fname)
        else:
             print("Incorrect password")
             exit()

        



print("Welcome to M-Banking ")
fname = input("Enter Username: ")
pwd = input("Enter password: ")
Authencication()


print("Kindly choose which service you would like to access")
print("1.DEPOSIT")
print("2.WITHDRAWAL")
print("3.CHECK BALANCE")
options = input(": ")

if options == "1":
     Deposit()
elif options == "2":
     Withdraw()
elif options == "3":
     Checkbal()
else:
     print("Invalid input")
     exit()
