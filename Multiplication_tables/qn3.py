"""3. Print the following. Learn how to use print with formatting
Learn how to print ********* using formatted print
My Tables
Table  1
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
**********
Table  2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
**********
Table  3
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
**********
End of tables """

print("Question 3")
print("My Tables")
asteriks='*'*10
for i in range(1,4):
    print("Table",i)
    for j in range(1,6):
        print(i,"*",j,"=",i*j)
    print("{}".format(asteriks),"\n")    
print("End of tables")
print("\n")