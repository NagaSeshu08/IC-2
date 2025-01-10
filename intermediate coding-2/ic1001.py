def remove_element(arr, key):
    count = 0
23    for i in range(len(arr)):
        if arr[i] != key:
            arr[count] = arr[i]
            count += 1
    return count

def main():
    # Take input for the list of integers
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    
    key = int(input("Enter the key to remove: "))
    
    new_length = remove_element(arr, key)
    
    print(f"Number of elements not equal to {key}: {new_length}")
    print("Updated array:", end=" ")
    
    for i in range(new_length):
        print(arr[i], end=" ")
    
    print()

if __name__ == "__main__":
    main()
