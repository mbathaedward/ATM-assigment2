#initilize user starting balane 
balance = 1000

#displaying user menu options until user chooses to exit
while True:
    print("\nATM MENU")
    print("1.check balance")
    print("2.deposit money")
    print("3.withdraw money")
    print("4.Exit")

#Getting the  users inputs
    choice = input("choose options here (1-4):")

#Handle each menu option using if-elif-else statements
    if choice == "1":
        print(f"Your balance is:ksh.{balance}")

    elif choice == "2":
        try:
            deposit_amount = float(input("please enter the amount to deposit to your account:"))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"ksh.{deposit_amount} has been deposited and your ksh.{balance}")
            else:("deposit amount must be positive")
        except ValueError:
            print("invalid value.please enter a numeric value")

    elif choice == "3":
        try:
            withdraw_amount = float(input("please enter amount to withdraw:"))
            if withdraw_amount >0:
                if withdraw_amount <= balance:
                    balance -=withdraw_amount
                    print(f"ksh.{withdraw_amount} has been withdrawn.new balancce is: {balance}")
                else:
                    print("insuffient balance for the withdrawal.")
            else:
                print("amount to withdrwal must be positive")
        except ValueError:
            print("invalid input.please enter a numeric amount")
                        


    elif choice == "4":
        print("thanks for using our services byebye!")
        break
    else:
        print("invalid choice please enter a valid option")

        



