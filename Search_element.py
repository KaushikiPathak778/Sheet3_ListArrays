arr=list(map(int,input("Enter the elements of the list: ").split()))
num=int(input("Enter the element you want to search: "))
if num in arr:
    print("The searched element is present in the given list.")  
else:
    print("The searched element is not present in the given list.")   
