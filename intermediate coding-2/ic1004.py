def merge_strings(file1, file2, file3):
    # Open the files and read the strings
    with open(file1, 'r') as f1:
        str1 = f1.read().strip()  # Read and remove any extra whitespace

    with open(file2, 'r') as f2:
        str2 = f2.read().strip()  # Read and remove any extra whitespace

    # Initialize an empty result string
    str3 = []

    # Get the minimum length of the two strings to merge alternatively
    min_length = min(len(str1), len(str2))

    # Merge alternatively
    for i in range(min_length):
        str3.append(str1[i])
        str3.append(str2[i])

    # Append the remaining characters from the longer string
    str3.append(str1[min_length:])  # Remaining characters from str1
    str3.append(str2[min_length:])  # Remaining characters from str2

    # Join the list to form the final merged string
    str3 = ''.join(str3)

    # Write the merged string to file3
    with open(file3, 'w') as f3:
        f3.write(str3)

    print("Merged string written to file3.")

# Example usage:
merge_strings('file1.txt', 'file2.txt', 'file3.txt')
