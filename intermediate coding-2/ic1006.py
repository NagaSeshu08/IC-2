def remove_zeros(arr):
    # Count the number of zeros in the array
    zero_count = arr.count(0)
    
    # Create a list of non-zero elements
    k = [x for x in arr if x != 0]
    
    # Add the zeros at the end
    k.extend([0] * zero_count)
    
    return k

# Input array
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Calling the function
result = remove_zeros(arr)

# Printing the result
print(result)
