def remove_duplicates(arr):
    if len(arr) == 0:
        return 0
    
    index = 1  # Points to the next unique position
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[index] = arr[i]
            index += 1
    
    return index

def main():
    n = int(input("Enter the number of elements in the array: "))
    
    if n <= 0:
        print("Invalid array size.")
        return
    
    arr = []
    print(f"Enter {n} sorted integers: ")
    for i in range(n):
        arr.append(int(input()))
    
    new_length = remove_duplicates(arr)
    
    print(f"Number of unique elements: {new_length}")
    print("Updated array:", end=" ")
    
    for i in range(new_length):
        print(arr[i], end=" ")
    
    print()

if __name__ == "__main__":
    main()
