arr=list(map(int,input("Enter elements of the list: ").split()))
odd_elements=[]
even_elements=[]
for num in arr:
    if num%2 == 0:
        even_elements.append(num)
    else:
        odd_elements.append(num)
print("Odd elements:",odd_elements)
print("Even elements:",even_elements)
