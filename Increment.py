array=list(map(int,input("Enter the elements of the array: ").split()))
incre=int(input("Enter the number by which you want to increment the value of elements of the array: "))
new_array=list(map(lambda x:x+incre,array))
print("Incremented array is:",new_array)
