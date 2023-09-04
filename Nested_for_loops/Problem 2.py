######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number upto 12 rows.

for i in range(7,17):
    for j in range(1,13):
        print(f"{i} * {j} = ",i*j)
    print("\n")    