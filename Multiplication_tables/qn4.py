"""4.Print the following
My Tables
Table  10
10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
**********
Table  8
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
**********
Table  6
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
**********
Table  4
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
**********
Table  2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
**********
End of tables """

print("Question 4")
print("My Tables")
asteriks='*'*10
for i in range(10,1,-2):
    print("Table",i)
    for j in range(1,6):
        print(i,"*",j,"=",i*j)
    print("{}".format(asteriks),"\n")    
print("End of tables")
print("\n")