n=input(input("enter how many numbers you want in this series:0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……"))
first=0
second=1
for i in range(n):
    print(first)
    temp=first
    temp=first 
    first=second
    second=temp+second
