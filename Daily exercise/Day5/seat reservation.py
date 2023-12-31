"""
Problem #1
Write a program for seat reservation in a theatre.
You can decide on the configuaration of the seats (no of rows and no of seats in each row, and a passage in between)
When the user asks for tickets, you need to provide them tickets in the form of seat no.
For eg, User ask for 3 seats in the middle. Output is F11, F12 , F13
Print the theatre configuaration at the end of each transaction.
"""

#Function to print the theatre seating arrangements
def print_theatre_configuration(rows, seats_in_a_row, seats):
    print("Theatre Configuration:")
    for row in range(1, rows + 1):
        for seat in range(1, seats_in_a_row + 1):
            if seat == seats_in_row // 2 + 1: #To print the passage width in the middle of the theatre
                print("||", end=" ")
            seat_label = f"{chr(row + 64)}{seat}" # seat_label=A1 or B4 or B5
            if (row, seat) in seats:
                print(seat_label, end=" ") 
            else:
                print("XX", end=" ")  # Mark booked seats with XX
        print()

#Function to create booked tickets and update the remaining seats available
def book_tickets(seats, buy_tickets):
    if len(buy_tickets) > len(seats):
        print("Sorry, not enough seats available -_-.")
        available_seats = seats
        return False,available_seats

    booked_seats = buy_tickets
    available_seats = []
    for seat in seats:
        if seat not in booked_seats:
            available_seats.append(seat)

    return booked_seats, available_seats

#main program
rows = 10           #Total no. of rows in the theatre
seats_in_row = 10   #Total no.of seats in each row
#passage_width = 2
seats = []
for row in range(1, rows + 1):
    for seat in range(1, seats_in_row + 1):
        seats.append((row, seat))# Append a tuple (row, seat) to the list

while True:
        print_theatre_configuration(rows, seats_in_row, seats)        
        num_tickets = int(input("Enter the number of tickets you want (0 to exit): "))
        
        if num_tickets == 0:
            print("Thank you!")
            break
        
        
        buy_tickets=[]
        for i in range(num_tickets):
            print(f"Enter the details of ticket{i+1}:")
            row_chr = input("Enter the row number of your seat: ").upper()
            row = ord(row_chr) - 64
            seat = int(input("Enter the seat(col) number of your seat: "))
            buy_tickets.append((row,seat))# Append a tuple (row, seat) to the list

        booked_seats,seats = book_tickets(seats, buy_tickets)

        if booked_seats:
            print("Successfully booked seats:", end=" ")
            for row, seat in booked_seats:
                print(f"{chr(row + 64)}{seat}", end=" ")
            print()
        else:
            print("Unable to book tickets")



#output
# Theatre Configuration:
# A1 A2 A3 A4 A5 || A6 A7 A8 A9 A10 
# B1 B2 B3 B4 B5 || B6 B7 B8 B9 B10 
# C1 C2 C3 C4 C5 || C6 C7 C8 C9 C10 
# D1 D2 D3 D4 D5 || D6 D7 D8 D9 D10 
# E1 E2 E3 E4 E5 || E6 E7 E8 E9 E10 
# F1 F2 F3 F4 F5 || F6 F7 F8 F9 F10 
# G1 G2 G3 G4 G5 || G6 G7 G8 G9 G10 
# H1 H2 H3 H4 H5 || H6 H7 H8 H9 H10 
# I1 I2 I3 I4 I5 || I6 I7 I8 I9 I10 
# J1 J2 J3 J4 J5 || J6 J7 J8 J9 J10 
# Enter the number of tickets you want (0 to exit): 3
# Enter the details of ticket1:      
# Enter the row number of your seat: A 
# Enter the seat(col) number of your seat: 3
# Enter the details of ticket2:
# Enter the row number of your seat: A
# Enter the seat(col) number of your seat: 4
# Enter the details of ticket3:
# Enter the row number of your seat: A 
# Enter the seat(col) number of your seat: 5
# Successfully booked seats: A3 A4 A5 
# Theatre Configuration:
# A1 A2 XX XX XX || A6 A7 A8 A9 A10
# B1 B2 B3 B4 B5 || B6 B7 B8 B9 B10
# C1 C2 C3 C4 C5 || C6 C7 C8 C9 C10
# D1 D2 D3 D4 D5 || D6 D7 D8 D9 D10
# E1 E2 E3 E4 E5 || E6 E7 E8 E9 E10
# F1 F2 F3 F4 F5 || F6 F7 F8 F9 F10
# G1 G2 G3 G4 G5 || G6 G7 G8 G9 G10
# H1 H2 H3 H4 H5 || H6 H7 H8 H9 H10
# I1 I2 I3 I4 I5 || I6 I7 I8 I9 I10
# J1 J2 J3 J4 J5 || J6 J7 J8 J9 J10
# Enter the number of tickets you want (0 to exit):