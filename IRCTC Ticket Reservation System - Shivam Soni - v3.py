import time
# Declare Variables
s_balance = 10000
c_balance = 15000
current_pin = "1234"

# Declare colors
c_red = '\033[91m'
c_green = '\033[32m'
c_yellow = '\33[93m'
c_magenta = '\033[35m'
c_blue = '\33[34m'
c_end = '\033[0m'

# Formation of Cabin list
cabin = list()
for a in range(1, 21):
    cabin.append(a)
fname = list()
for b in range(1, 21):
    fname.append(b)
lname = list()
for c in range(1, 21):
    lname.append(c)
agep = list()
for d in range(1, 21):
    agep.append(d)

# Program
while True:
    print(c_green + '\nWelcome to IRCTC Ticket Booking System,' + c_end,
          "\n 1 - Book a Ticket \n 2 - Check Seat Reservation of Cabin \n 3 - Cancel Ticket \n 4 - Show Details of Ticket \n 5 - View Balance\n 6 - Exit App")
    selection = input("\nPlease enter Your Selection (1/2/3/4/5) - ")

    # Function to Handle Errors
    def error(e_code):
        if e_code == "inv_acc":
            print(c_red + "\tPlease try again.\n\tError Code: Invalid Account" + c_end)
        elif e_code == "inc_pin":
            print(c_red + "\tPlease try again.\n\tError Code: Incorrect PIN" + c_end)
        elif e_code == "inc_bal":
            print(c_red + "\tInsufficient Balance\n" + c_end)
        elif e_code == "inc_amt":
            print(c_red + "\tPlease try again. Transaction Cancelled\n" + c_end)
        elif e_code == "inc_sel":
            print(c_red + "\tPlease try Again.\n\tError Code: Invalid Selection" + c_end)
        else:
            print(c_red + "\tPlease try again.\n\tError Code:", e_code, "\n" + c_end)
        time.sleep(2)

    # Verification Animation
    def verf():
        x = 0
        while x != 4:
            time.sleep(0.35)
            print(c_magenta + "\tVerifying", x * "." + c_end)
            x += 1

    # Booking Seats
    if selection == "1":
        while True:
            try:
                seat_num = int(input('\tPlease Enter the Seat Number that You want to Book (1-20) - '))
                if seat_num <= 20 and seat_num != 0:
                    break
                else:
                    error("Please Enter Seat Number Between 1-20")
            except ValueError:
                error("Please use only numbers, try again")

        if cabin[seat_num - 1] == seat_num:

            # For First Name
            temp1 = input("\tPlease Enter Passenger's First Name - ")
            while not temp1.isalpha():
                error("Please use only letters, try again")
                temp1 = input("\tPlease Enter Passenger's First Name - ")

            # For Last Name
            temp2 = input("\tPlease Enter Passenger's Last Name - ")
            while not temp2.isalpha():
                error("Please use only letters, try again")
                temp2 = input("\tPlease Enter Passenger's Last Name - ")

            # For Age
            temp3 = input("\tPlease Enter Passenger's Age - ")
            while not temp3.isnumeric():
                error("Please use only Numbers, try again")
                temp3 = input("\tPlease Enter Passenger's Age - ")

            verf()

            # Payment
            print("How would you like to pay? (Savings/ Current)")
            acc = str(input("\t1. Savings \n\t2. Current\n\t--- "))
            if acc == "1":
                acc = "Savings"
                balance = s_balance
            elif acc == "2":
                acc = "Current"
                balance = c_balance
            else:
                error("inv_acc")
                continue

            print("The Available balance in Your", acc, " Account is ", int(balance))
            amount = 100
            verify = str(input(c_blue + "Are you sure that you want to Pay IRCTC Rs." + str(amount) + " (Y/N) --- " + c_end))
            # Debit process
            if verify == "y" or verify == "yes":
                temp4 = input("Please Enter Your PIN --- ")
                if temp4 == current_pin:
                    if amount <= balance and acc == "Savings":
                        s_balance -= amount
                        balance = s_balance
                    if amount <= balance and acc == "Current":
                        c_balance -= amount
                        balance = c_balance
                    if amount > balance:
                        error("inc_bal")
                        continue

                    verf()
                    print("Available balance is ", balance, "in", acc, " account\nThanks For choosing us!" + c_end)
                    time.sleep(2)

                    # Add Details to cabin list
                    cabin.pop(seat_num - 1)
                    cabin.insert(seat_num - 1, c_yellow + 'B' + c_end)
                    # For First name
                    fname.pop(seat_num - 1)
                    fname.insert(seat_num - 1, temp1)
                    # For Last Name
                    lname.pop(seat_num - 1)
                    lname.insert(seat_num - 1, temp2)
                    # For Age
                    agep.pop(seat_num - 1)
                    agep.insert(seat_num - 1, temp3)
                    # Success message
                    print(c_green + "\nPassenger's Ticket Has Been Booked Successfully!")
                    print(c_yellow + "\tCustomer Name :", fname[seat_num - 1].title(), lname[seat_num - 1].title(), "\n\tAge : ",
                          agep[seat_num - 1], "\n\tSeat Number : ", str(seat_num) + c_end)
                    time.sleep(3)
                    continue
                else:
                    error("inc_pin")
                    continue
            else:
                error("inc_amt")
                continue
        else:
            error("This seat is already booked, Please try other seat")

    #   For Checking Check Seat Reservation of Cabin
    elif selection == "2":
        print("Here is The Status of Reservation of Tickets in Cabin,", c_yellow + "Highlighted" + c_end, "seats are booked")
        for k in cabin:
            print(k, end="  ")
        print("\n")
        time.sleep(3)

    #   For Cancelling Ticket
    elif selection == "3":
        while True:
            try:
                seat_num = int(input('Please Enter the Seat Number that you want to Cancel (1-20) - '))
                if seat_num <= 20 and seat_num != 0:
                    break
                else:
                    error("Please Enter Seat Number Between 1-20")
            except ValueError:
                error("Please use only numbers, try again")
        if cabin[seat_num - 1] == seat_num:
            error("This Seat is not Booked")
        else:
            print(c_yellow + "\tCustomer Name :", fname[seat_num - 1].title(), lname[seat_num - 1].title(), "\n\tAge : ",
                  agep[seat_num - 1] + c_end)
            temp = input(c_red + "Are you Sure That You Want to Cancel this Ticket? (Y/N) - " + c_end)
            if temp == "y" or temp == "yes":
                cabin.pop(seat_num - 1)
                cabin.insert(seat_num - 1, seat_num)
                verf()
                print("Passenger's Ticket has been Cancelled Successfully")
            elif temp == "n" or temp == "no":
                break
            else:
                error("Invalid Selection")

    #   For Checking Details of Specific ticket
    elif selection == "4":
        while True:
            try:
                seat_num = int(input('Please Enter the Seat Number that you want details of (1-20) - '))
                if seat_num <= 20 and seat_num != 0:
                    break
                else:
                    error("Please Enter Seat Number Between 1-20")
            except ValueError:
                error("Please use only numbers, try again")
        if fname[seat_num - 1] == seat_num:
            print(c_green + "This Seat is not Booked\n" + c_end)
            time.sleep(1.5)
        else:
            print(c_yellow + "\tCustomer Name :", fname[seat_num - 1].title(), lname[seat_num - 1].title(),
                  "\n\tAge : ",
                  agep[seat_num - 1], "\n\tSeat Number : ", str(seat_num) + c_end)
            time.sleep(3)

    # Check Balance
    elif selection == "5":
        print(c_blue + "\nThe Available balance in Your Savings Account is ", str(c_yellow) + str(float(s_balance)) + c_end)
        print(c_blue + "The Available balance in Your Current Account is ", str(c_yellow) + str(float(c_balance)), "\n" + c_end)
        time.sleep(2)
        continue

    # Exiting Program
    elif selection == "6":
        print(c_blue + "Thanks For choosing us!\nHave a Wonderful Day" + c_end)
        time.sleep(2)
        quit()
    else:
        error("inc_sel")

#  Made By Shivam Soni
