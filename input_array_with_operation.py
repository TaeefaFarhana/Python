input_array=input("Enter integers : ")
array_split=input_array.split()
array=[int(i) for i in array_split]
print("Display array : ",array)
array_sqr=[int(i)*int(i) for i in array_split]
print("Square of array : ",array_sqr)
