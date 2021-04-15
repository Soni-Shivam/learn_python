import random
import time

# Declare colors
c_red = '\033[91m'
c_green = '\033[32m'
c_yellow = '\33[93m'
c_magenta = '\033[35m'
c_blue = '\33[34m'
c_end = '\033[0m'

# Declare Variables
trains_dict = {
    1: {"Name": "Rajdhani Express", "strt": "DELHI", "end": "MUMBAI"},
    2: {"Name": "Jan Shatabdi Express", "strt": "DELHI", "end": "PUNE"},
    3: {"Name": "Garib Rath Express", "strt": "DELHI", "end": "BHOPAL"},
    4: {"Name": "Intercity Express", "strt": "DELHI", "end": "BANGLORE"},
    5: {"Name": "Vande Bharat Express", "strt": "MUMBAI", "end": "DELHI"},
    6: {"Name": "Tejas Express", "strt": "MUMBAI", "end": "PUNE"},
    7: {"Name": "Gatiman Express", "strt": "MUMBAI", "end": "BHOPAL"},
    8: {"Name": "Mahamana Express", "strt": "MUMBAI", "end": "BANGLORE"},
    9: {"Name": "Uday Express", "strt": "PUNE", "end": "MUMBAI"},
    10: {"Name": "Vivek Express", "strt": "PUNE", "end": "DELHI"},
    11: {"Name": "Rajdhani Express", "strt": "PUNE", "end": "BHOPAL"},
    12: {"Name": "Jan Shatabdi Express", "strt": "PUNE", "end": "BANGLORE"},
    13: {"Name": "Garib Rath Express", "strt": "BHOPAL", "end": "MUMBAI"},
    14: {"Name": "Intercity Express", "strt": "BHOPAL", "end": "PUNE"},
    15: {"Name": "Vande Bharat Express", "strt": "BHOPAL", "end": "KANPUR"},
    16: {"Name": "Tejas Express", "strt": "BHOPAL", "end": "BANGLORE"}
}
mybookings = {}
mybookings ["bookings"] = {}

# Generate Random Seats
trains = list(trains_dict)
seats_l = []
for i in range(0, len(trains_dict)):
    seats_l.append(str(random.randint(10, 31)))
    trains_dict[trains[i]]["seats"] = seats_l[i]

# Generate Cabin
t_dict = {
    0: {"Name": "Rajdhani Express"},
    1: {"Name": "Jan Shatabdi Express"},
    2: {"Name": "Garib Rath Express"},
    3: {"Name": "Intercity Express"},
    4: {"Name": "Vande Bharat Express"},
    5: {"Name": "Tejas Express"},
    6: {"Name": "Gatiman Express"},
    7: {"Name": "Mahamana Express"},
    8: {"Name": "Uday Express"},
    9: {"Name": "Vivek Express"},
    10: {"Name": "Rajdhani Express"},
    11: {"Name": "Jan Shatabdi Express"},
    12: {"Name": "Garib Rath Express"},
    13: {"Name": "Intercity Express"},
    14: {"Name": "Vande Bharat Express"},
    15: {"Name": "Tejas Express"}
}

for i in range(0, len(t_dict)):
    t_dict[i]["Seatn"] = {}
    s = int(seats_l[i])
    for a in range(1, s):
        t_dict[i]["Seatn"][a] = {}
        t_dict[i]["Seatn"][a]["First name"] = "NA"
        t_dict[i]["Seatn"][a]["Last name"] = "NA"
        t_dict[i]["Seatn"][a]["Age"] = "NA"
        t_dict[i]["Seatn"][a]["Coach"] = "NA"

# UI
while True:
    # Function to Handle Errors
    def error(e_code):
        print(c_red + "\tPlease try again.\n\tError Code:", e_code, "\n" + c_end)
        time.sleep(2)


    print(c_green + '\nWelcome to IRCTC Ticket Booking System,' + c_end,
          "\n 1 - Book a Ticket \n 2 - Check Availability and Plan Journey \n 3 - My Bookings \n 4 - PNR Enquiry \n 5 - Exit App")
    selection = input("\nPlease enter Your Selection (1/2/3/4/5) - ")
    # Booking Seats
    if selection == "1":
        # Value check
        while True:
            strt = input("Please Enter Departure Location - ")
            strt = strt.upper()
            if strt == "DELHI" or strt == "MUMBAI" or strt == "PUNE" or strt == "BHOPAL":
                break
            else:
                error("Please Enter a valid Station (Delhi/Mumbai/Bhopal/Pune/Banglore)")
        filt = []
        print("\nHere are the Matching Trains -")

        # Filtering based on Query
        for i in range(len(trains_dict)):
            if strt.upper() == trains_dict[trains[i]]["strt"]:
                filt.append(i)

        # Print the names of the columns.
        print("{:<35} {:<20} {:<20} {:<20}".format((c_yellow + 'Train'), 'From', 'To',
                                                   ('Seats Available' + c_end)))
        # Print each data item
        for i in range(len(filt)):
            print("{:<35} {:<20} {:<20} {:<20}".format(c_green + (trains_dict[trains[filt[i]]]["Name"]),
                                                       (trains_dict[trains[filt[i]]]["strt"]),
                                                       (trains_dict[trains[filt[i]]]["end"]),
                                                       str((trains_dict[trains[filt[i]]]["seats"])) + c_end))

        # Value check
        while True:
            end = input("\nPlease Enter Destination - ")
            end = end.upper()
            if end == "DELHI" or end == "MUMBAI" or end == "PUNE" or end == "BHOPAL":
                break
            else:
                error("Please Enter a valid Station (Delhi/Mumbai/Bhopal/Pune/Banglore)")
        print("\nHere are the Matching Trains -")
        filt = []
        for i in range(len(trains_dict)):
            if end.upper() == trains_dict[trains[i]]["end"] and strt.upper() == trains_dict[trains[i]]["strt"]:
                filt.append(i)

        # Print the names of the columns.
        print("{:<35} {:<20} {:<20} {:<20}".format((c_yellow + 'Train'), 'From', 'To',
                                                   ('Seats Available' + c_end)))
        # Print each data item
        for i in range(len(filt)):
            print("{:<35} {:<20} {:<20} {:<20}".format(c_green + (trains_dict[0

                ns[filt[i]]]["Name"]),
                                                       (trains_dict[trains[filt[i]]]["strt"]),
                                                       (trains_dict[trains[filt[i]]]["end"]),
                                                       str((trains_dict[trains[filt[i]]]["seats"])) + c_end))
        # Value check
        while True:
            book = input("Do you want to Book this train? (YES/NO) - ")

            # Reserve Seat
            if book == 'y':
                # Check Seats Availability
                if int((trains_dict[trains[filt[0]]]["seats"]))>= 1:
                    temp0 = input("Please Enter the Coach (A1/A2/A3/SC) - ")

                    while True:
                        if temp0.upper() == "A1":
                            tc_w = "One Thousand Rupees Only"
                            tc_v = "1000"
                            break
                        elif temp0.upper() == "A2":
                            tc_w = "Seven Hundred Rupees Only"
                            tc_v = "700"
                            break
                        elif temp0.upper() == "A3":
                            tc_w = "Five Hundred Rupees Only"
                            tc_v = "500"
                            break
                        elif temp0.upper() == "SC":
                            tc_w = "Three Hundred Rupees Only"
                            tc_v = "300"
                            break
                        else:
                            error("Please enter a valid selection")
                            temp = input("Please Enter the Coach (A1/A2/A3/SC) - ")

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

                    # Locating Avaiable Seats
                    for i in range(1, len(t_dict)):
                        if t_dict[i]["Name"] == trains_dict[trains[filt[0]]]["Name"]:
                            t_num = i
                    # Adding Customer Info to Database
                    seat_num = random.randint(1, int(seats_l[t_num]))
                    t_dict[t_num]["Seatn"][seat_num]["First name"] = temp1.title()
                    t_dict[t_num]["Seatn"][seat_num]["Last name"] = temp2.title()
                    t_dict[t_num]["Seatn"][seat_num]["Age"] = str(temp3).zfill(2)
                    t_dict[t_num]["Seatn"][seat_num]["Coach"] = temp0.upper()
                    trains_dict[trains[filt[0]]]["seats"] = int(trains_dict[trains[filt[0]]]["seats"]) - 1
                    # For My Bookings Functinality
                    # bookings += 1
                    # mybookings[bookings]["Train Number"] = str(t_num).zfill(2)
                    pnr: str = str(t_num).zfill(2) + str(seat_num) + str("PNR.Num")
                    # mybookings[bookings]["PNR"] = pnr

                    # Success message
                    print(c_green + "\nPassenger's Ticket Has Been Booked Successfully!")
                    print(c_yellow + "\tCustomer Name :", t_dict[t_num]["Seatn"][seat_num]["First name"].title(),
                          t_dict[t_num]["Seatn"][seat_num]["Last name"].title(),
                          "\n\tAge : ",  t_dict[t_num]["Seatn"][seat_num]["Age"], "\n\tTrain : ",
                          t_dict[t_num]["Name"],"\n\tCoach : ",
                          t_dict[t_num]["Seatn"][seat_num]["Coach"],"\n\tSeat Num : ",
                          seat_num,"\n\tPNR : ", str(pnr) + c_end)
                    time.sleep(3)
                    break
                else:
                    error("Sorry, All Seats In this Train Are booked")

            # Cancel
            elif book == "no" or book == "n":
                break
            else:
                error("Please Enter a valid Selection (YES/NO)")

    # Checking Availability
    if selection == "2":
        # Print the names of the columns.
        print("{:<35} {:<20} {:<20} {:<20}".format((c_yellow + 'Train'), 'From', 'To', ('Seats Available' + c_end)))

        # Print each data item
        for i in range(len(trains_dict)):
            print("{:<35} {:<20} {:<20} {:<20}".format(c_green + (trains_dict[trains[i]]["Name"]),
                                                       (trains_dict[trains[i]]["strt"]),
                                                       (trains_dict[trains[i]]["end"]),
                                                       str((trains_dict[trains[i]]["seats"])) + c_end))
        time.sleep(3)
        continue

    # PNR Enquiry
    if selection == "4":
        pnr_entry = input("Please Enter Your PNR Number - ")
        t_num_entry = pnr_entry[0,1]
        s_num_entry = pnr_entry[2,3]
        t_dict[t_num_entry]["Seatn"][s_num_entry]
        print(c_yellow + "\tCustomer Name :", t_dict[t_num_entry]["Seatn"][s_num_entry]["First name"].title(),
             t_dict[t_num_entry]["Seatn"][s_num_entry]["Last name"].title(),
             "\n\tAge : ", t_dict[t_num]["Seatn"][s_num_entry]["Age"], "\n\tCoach : ",
             t_dict[t_num_entry]["Seatn"][s_num_entry]["Coach"], "\n\tPNR : ", str(pnr_entry) + c_end)

    # Quit Program
    if selection == "5":
        temp = input("Are you Sure you want to Exit? (Y/N)")
        if temp.lower() == "y":
            quit()
        else:
            continue

