arr=list(map(int,input("Enter the elements of the array: ").split()))
sum=0; 
for i in range (len(arr)):
    sum=sum+arr[i]
print(sum)