import re

def reverse_string(s):
    
    clean_string = re.sub(r'[,.]', '', s)
    
   
    words = clean_string.split()
    
   
    reverse_string = ' '.join(reversed(words))
    
    return reverse_string


input_string = input("Enter a string: ")


result = reverse_string(input_string)
print(result)
