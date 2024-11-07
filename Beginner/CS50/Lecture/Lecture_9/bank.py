# initial version

balance = 0

def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance: ", balance)

def deposit(n):
    balance += n

def withdraw(n):
    balance -= n


if __name__ == "__main__":
    main()

# fixing errors and next version introducing global to function

balance = 0

def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance: ", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main() 