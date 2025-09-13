arr=list(map(int,input("Enter the elements of the list: ").split()))
print("Negative numbers are: ")
for num in arr:
    if num<0:
        print(num)