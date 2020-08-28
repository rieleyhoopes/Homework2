# I am going to create a code that sorts an array from least to greatest
# I am first going to create an array of number

Num_Array = [2, 8, 19, 43, -12, 0, 83, 108, 7]
# This will display the array to the viewer
print(Num_Array)

# I would like to show the number of items in the array
Array_Count = len(Num_Array)
print("The total number of items in the array is: " +str(Array_Count))

# Now I will find the average value of the array
Array_Sum = sum(Num_Array)
print("The average value of the array is: " + str(Array_Sum / Array_Count))

#Showing the minimum and maximum values of the array
print(str(min(Num_Array)) + " is the minimum of the array and " + str(max(Num_Array)) + " is the maximum value of the array")

#This will sort the values in the array from least to greatest
Num_Array.sort()
# This will print the sorted array
print("Sorted from least to greatest:" + str(Num_Array) )