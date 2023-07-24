print("Welcome to SBI Bank \n \n Insert your card")

password = 1234
balance = 10000
choice = 0

pin = int(input("Enter your 4-Digit pin \n"))

if pin == password:
    while choice != 4:
        print("********* Menu ********")
        print("1- Balance")
        print("2- Deposit")
        print("3- Withdraw")
        print("4- Cancel")

        choice = int(input("\n Enter your option: \n"))

        if choice == 1:
            print("Balance = Rs", balance)
        elif choice == 2:
            dep = int(input("Enter your deposit: Rs "))
            balance += dep
            print("\n Deposited Amount: Rs ", dep)
            print("Balance = Rs ", balance)
        elif choice == 3:
            wit = int(input("Enter your deposit: Rs "))
            balance -= wit
            print("\n Withdrawal Amount: Rs ", wit)
            print("Balance = Rs ", balance)
        elif choice == 4:
            print("Session Ended!! GoodBye")
        else:
            print("Invalid Entry!!")
else:
    print("Pin Incorrect!! Try Again")