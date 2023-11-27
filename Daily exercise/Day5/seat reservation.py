"""
Problem #1
Write a program for seat reservation in a theatre.
You can decide on the configuaration of the seats (no of rows and no of seats in each row, and a passage in between)
When the user asks for tickets, you need to provide them tickets in the form of seat no.
For eg, User ask for 3 seats in the middle. Output is F11, F12 , F13
Print the theatre configuaration at the end of each transaction.
"""

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

def book_tickets(seats, num_tickets):
    if num_tickets > len(seats):
        print("Sorry, not enough seats available -_-.")
        return []

    booked_seats = seats[:num_tickets]
    available_seats = seats[num_tickets:]

    return booked_seats, available_seats

rows = 10
seats_in_row = 10
passage_width = 2
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

        booked_seats,seats = book_tickets(seats, num_tickets)

        if booked_seats:
            print("Successfully booked seats:", end=" ")
            for row, seat in booked_seats:
                print(f"{chr(row + 64)}{seat}", end=" ")
            print()
        else:
            print("Unable to book tickets")
