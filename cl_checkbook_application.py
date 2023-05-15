balance=1000
print("~~~ Welcome to your terminal checkbook!~~~")
print("\n1)\tBalance\n2)\tWithdraw\n3)\tDeposit\n4)\tQuit\n")
     
while True:
    Option=int(input("Enter Option: "))
    if Option==1:
        print("Balance $",balance)
        print("What would you like to do today? ")
        
    elif Option==2:
        print("Balance $",balance)
        Withdraw=float(input("Enter your desired withdraw amount $ "))

        if Withdraw>0 and Withdraw<=balance:
            balance -= Withdraw
            print("Your new balance is:$",balance)
            print("What would you like to do today? ")
            
        elif Withdraw>balance:
            print("Not applicable. Insufficient funds.")
            print("What would you like to do today? ")

        else:
            print("No withdraw made")
            print("What would you like to do today? ")

    elif Option==3:
        print("Balance  $ ",balance)
        Deposit=float(input("Enter your desired deposit amount $"))
        if Deposit>0:
            balance += Deposit
            print("Your new balance is: $",balance)
            print("What would you like to do today? ")
            
            
        else:
            print("None deposit made")
            print("What would you like to do today? ")

    elif Option==4:
        print('Goodbye.')
        exit()

    else:
        print('invalid choice!')
        