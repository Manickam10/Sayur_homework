"""
Problem #2
Same problem as above. Also calculate tickets price. 
Firsrt 3 rows - Rs100
Rows 4 to 12 - Rs 200
Rows 13 till top - Rs 300.
3 seats close to the wall on both sides costs less than the other seats in the same row."""

#Function to print the theatre seating arrangements
def print_theatre_configuration(rows, seats_in_a_row, seats):
    print("Theatre Configuration:")
    for row in range(1, rows + 1):
        for seat in range(1, seats_in_a_row + 1):
            if seat == seats_in_row // 2 + 1: #To print the passage width in the middle of the theatre
                print("||", end=" ")
            seat_label = f"{chr(row + 64)}{seat}"
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

#Function to calculate ticket price
def calculate_ticket_price(row, seat, seats_in_a_row):
    if row <= 3:
        price = 100 #Firsrt 3 rows - Rs100
    elif 4 <= row <= 12:
        price = 200 #Rows 4 to 12 - Rs 200
    else:
        price = 300 #Rows 13 till top - Rs 300

    if seat <= 3 or seat >= seats_in_a_row - 2:
        discount= 0.9  # 10% discount for seats close to the wall
    else:
        discount= 1.0
    return price * discount

#main program
rows = 10
seats_in_row = 10
#passage_width = 2
seats = []
for row in range(1, rows + 1):
    for seat in range(1, seats_in_row + 1):
        seats.append((row, seat))

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
            buy_tickets.append((row,seat))

        booked_seats,seats = book_tickets(seats, buy_tickets)

        if booked_seats:
            total_price = 0
            print("Successfully booked seats:", end=" ")
            for row, seat in booked_seats:
                price = calculate_ticket_price(row, seat, seats_in_row) 
                total_price += price
                print(f"{chr(row + 64)}{seat} (Rs{price})", end=" ")

            print("\nTotal Price: Rs", total_price)
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
# Enter the row number of your seat: G
# Enter the seat(col) number of your seat: 6
# Enter the details of ticket2:
# Enter the row number of your seat: G
# Enter the seat(col) number of your seat: 7
# Enter the details of ticket3:
# Enter the row number of your seat: G
# Enter the seat(col) number of your seat: 8
# Successfully booked seats: G6 (Rs200.0) G7 (Rs200.0) G8 (Rs180.0) 
# Total Price: Rs 580.0
# Theatre Configuration:
# A1 A2 A3 A4 A5 || A6 A7 A8 A9 A10
# B1 B2 B3 B4 B5 || B6 B7 B8 B9 B10
# C1 C2 C3 C4 C5 || C6 C7 C8 C9 C10 
# D1 D2 D3 D4 D5 || D6 D7 D8 D9 D10
# E1 E2 E3 E4 E5 || E6 E7 E8 E9 E10
# F1 F2 F3 F4 F5 || F6 F7 F8 F9 F10
# G1 G2 G3 G4 G5 || XX XX XX G9 G10
# H1 H2 H3 H4 H5 || H6 H7 H8 H9 H10
# I1 I2 I3 I4 I5 || I6 I7 I8 I9 I10
# J1 J2 J3 J4 J5 || J6 J7 J8 J9 J10
# Enter the number of tickets you want (0 to exit):