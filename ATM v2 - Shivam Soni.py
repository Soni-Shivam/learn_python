import time
s_balance = 10000
c_balance = 15000
pin = input("Welcome to the ATM\nPlease Enter your account PIN \n")
current_pin = "1234"

while pin != current_pin:
    print("Please try again.\nError Code: Invalid Pin")
    pin = input("\nPlease Enter your account PIN \n")

while pin == current_pin:
    print(' 1 - View Balance \n 2 - Withdraw \n 3 - Deposit \n 4 - Change PIN\n 5 - Exit ')
    selection = input("Please enter Your Selection\n")

    def error(e_code):
        if e_code == "inv_acc":
            print("Please try again.\nError Code: Invalid Account")
        elif e_code == "inc_pin":
            print("Please try again.\nError Code: Incorrect PIN")
        elif e_code == "inc_amt":
            print("Please try again.\nError Code: Wrong Amount")
        elif e_code == "inc_bal":
            print("Insufficient Balance\n")
        elif e_code == "pins_match":
            print("The PINs don't match, Please try again.")
        elif e_code == "inc_sel":
            print("Please try Again.\nError Code: Invalid Selection")
        time.sleep(3)

    def verf():
        x = 0
        while x != 4:
            time.sleep(0.35)
            print("Verifying", x * ".")
            x += 1

    if selection == "1":
        print("\nThe Available balance in Your Savings Account is ", float(s_balance))
        print("The Available balance in Your Current Account is ", float(c_balance), "\n")
        time.sleep(2)
        continue
    if selection == "2":
        print("Choose the account that you want to withdraw from")
        acc = str(input("1. Savings \n2. Current \n"))
        if acc == "1":
            acc = "Savings"
            balance = s_balance
        elif acc == "2":
            acc = "Current"
            balance = c_balance
        else:
            error("inv_acc")
            continue
        print("The Available balance in Your", acc, " Account is ", int(balance),
              "\nPlease Enter the amount you want to withdraw from your", acc, " account\n")
        amount = int(input())
        verify = str(input("Is this the correct amount, Y/N ? " + str(amount) + "\n"))
        if verify == "y":
            temp4 = input("\nPlease Enter Your PIN\n")
            if temp4 == current_pin:
                verf()
                if amount <= balance and acc == "Savings":
                    s_balance -= amount
                    balance = s_balance
                if amount <= balance and acc == "Current":
                    c_balance -= amount
                    balance = c_balance
                if amount > balance:
                    error("inc_bal")
                    continue
                print("Available balance is ", balance, "in", acc, " account\nThanks For choosing us!")
                time.sleep(3)
                continue
            else:
                error("inc_pin")
                continue
        else:
            error("inc_amt")
            continue
    if selection == "3":
        print("\tChoose the account that you want to deposit to")
        acc = str(input("\t1. Savings \n\t2. Current \n\t"))
        if acc == "1":
            acc = "Savings"
            balance = s_balance
        elif acc == "2":
            acc = "Current"
            balance = c_balance
        else:
            error("inv_acc")
            continue
        print("\tThe Available balance in Your", acc, " Account is ", int(balance),
              "\n\tPlease Enter the amount you want to deposit to your", acc, " account\n")
        amount = int(input())
        verify = str(input("\t\tIs this the correct amount, Y/N ? " + str(amount) + "\n"))
        if verify == "y":
            temp4 = input("\nPlease Enter Your PIN\n")
            if temp4 == current_pin:
                verf()
                if acc == "Savings":
                    s_balance += amount
                    balance = s_balance
                if acc == "Current":
                    c_balance += amount
                    balance = c_balance
                print("\t\tAvailable balance is ", balance, "in", acc, " account\n\t\tThanks For choosing us!")
                time.sleep(3)
                continue
            else:
                error("inc_pin")
                continue
        else:
            error("inc_amt")
            continue
    if selection == "4":
        temp = input("Please Enter Current PIN For Verification\n")
        if temp == current_pin:
            temp2 = input("Please Enter a new PIN\n")
            temp3 = input("Please Enter the New Pin Once again for Confirmation\n")
            if temp2 == temp3:
                current_pin = temp2
                pin = current_pin
                verf()
                print("Your PIN was changed Successfully\nPlease note that this PIN is valid for this session only.")
                time.sleep(2)
                continue
            elif temp2 != temp3:
                error("pins_match")
                continue
        elif temp != current_pin:
            error("inc_pin")
            continue
    if selection == "5":
        print("Thanks For choosing us!\nHave a Wonderful Day")
        time.sleep(3)
        quit()
    else:
        error("inc_sel")
