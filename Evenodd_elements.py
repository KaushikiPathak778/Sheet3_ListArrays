arr=list(map(int,input("Enter elements of the list: ").split()))
even_count=0
odd_count=0
for num in arr:
    if num% 2== 0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("Absolute difference: ")
difference=abs(even_count-odd_count)
print(difference)
