array=list(map(int,input("Enter the numbers: ").split()))
maximum=array[0]
for num in array:
   if num>maximum:
       maximum=num
print("Maximum element in the given array is: ",maximum)
minimum=array[0]
for num in array:
   if num<minimum:
       minimum=num
print("Minimum element in the given array is: ",minimum)