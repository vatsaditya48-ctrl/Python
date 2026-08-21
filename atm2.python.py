# Simple ATM Simulator by aditya chauhan 11th commerce
#chapters covered: Getting started with python, loops, operators, if else elif, for loop while loop
balance =500000
bill=2700
credit_card_bill=40000
waterbill=3500
totaldues= bill+credit_card_bill+waterbill #Predefining dues
pin = "1234"
import time #saw this in a python video

steps = [
    "Initializing system...",
    "Loading configuration files...",
    "Verifying user credentials...",
    "Authenticating session...",
    "Establishing secure connection...",
    "Synchronizing local cache...",
    "Scanning available resources...",
    "Allocating memory...",
    "Loading required modules...",
    "Performing integrity checks...",
    "Encrypting temporary session...",
    "Preparing runtime environment...",
    "Optimizing performance...",
    "Finalizing initialization...",
    "Starting main services...",
    "System ready."
]

for step in steps:
    print(step)
    time.sleep(0.4) #0.4 seconds per line to be printed

print("===== Welcome to Python ATM =====")

entered_pin = input("Enter your 4-digit PIN: ") #authenticates with the actual pin

if entered_pin == pin:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("5. Check dues")
        print("6. Pay dues")

        choice = input("Enter your choice (1-6): ")  #core loop

        if choice == "1": #if statements
            print("Your balance is ₹", balance)

        elif choice == "2":
            amount = int(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount #chapter 5 operators
                print("₹", amount, "deposited successfully.")
                print("New Balance: ₹", balance)
            else:
                print("Invalid amount!")

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: ₹"))

            if amount <= balance and amount > 0:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining Balance: ₹", balance)
            elif amount > balance: #so the bankbalance dosent show negative
                print("Insufficient balance!")
            else:
                print("Invalid amount!")

        if choice== "5":
            print("Your dues are: Electricity", bill, "Credit Card bill:", credit_card_bill, "Water bill:", waterbill)
            
        if choice== "6": #second multi function if choise area
            print("What dues will you like to pay!")
            print("1. Electricity Bill")
            print("2. Credit card bill")
            print("3. Water bill")
            print("4 All dues")
        choice_2= int(input("Enter any option (1-4):"))
        if choice_2==1:
            print("An ammount of", bill, "is to be deducted")
            balance-=bill
            print(balance,"is your new balance")
        if choice_2==2:
            print("An ammount of", credit_card_bill, "is to be deducted")
            balance-=credit_card_bill
            print("Your new balance is", balance)
        if choice_2==3:
            balance-=waterbill
            print("An ammount of",waterbill,"is the be deducted")
        if choice_2==4:
            print("An ammount of", totaldues, "is to be deducted")
            balance-=totaldues
            print("Your new balance is:", balance)
        elif choice == "4":
            print("Thank you for using Python ATM!")
            break

        else:
            print("Invalid choice. Try again.")
else:
    print("Incorrect PIN!")
