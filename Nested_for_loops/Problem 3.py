######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print('\u2B1C',end='')  # White square
        else:
            print('\u2B1B',end='')  # Black square
    print()  # Move to the next row
