"""5. Print the following
My Tables
Table  1
Easy numbers
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10
Advanced numbers
1 * 11 = 11
1 * 12 = 12
1 * 13 = 13
1 * 14 = 14
1 * 15 = 15
1 * 16 = 16
1 * 17 = 17
1 * 18 = 18
1 * 19 = 19
1 * 20 = 20
**********
Table  2
Easy numbers
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
Advanced numbers
2 * 11 = 22
2 * 12 = 24
2 * 13 = 26
2 * 14 = 28
2 * 15 = 30
2 * 16 = 32
2 * 17 = 34
2 * 18 = 36
2 * 19 = 38
2 * 20 = 40
**********
Table  3
Easy numbers
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30
Advanced numbers
3 * 11 = 33
3 * 12 = 36
3 * 13 = 39
3 * 14 = 42
3 * 15 = 45
3 * 16 = 48
3 * 17 = 51
3 * 18 = 54
3 * 19 = 57
3 * 20 = 60
**********
End of tables"""

Easy_numbers=[1,2,3,4,5,6,7,8,9,10]
Advanced_numbers=[11,12,13,14,15,16,17,18,19,20]
asteriks='*'*10
print("My Tables")
for i in range(1,4):
    print("Table",i)
    print("Easy numbers")
    
    for j in range(1,len(Easy_numbers)+1):
        print(f"{i} * {Easy_numbers[j-1]} = {i * Easy_numbers[j-1]}")
    
    print("Advanced numbers")
    
    for j in range(1,len(Advanced_numbers)+1):
        print(f"{i} * {Advanced_numbers[j-1]} = {i * Advanced_numbers[j-1]}")
    
    print("{}".format(asteriks),"\n")

print("End of tables")
