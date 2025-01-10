def is_substring(main_str, sub_str):
    if sub_str in main_str:
        return sub_str
    else:
        return False

main_str = input("enter a string")

sub_str =  input("enter a sub_string")

result = is_substring(main_str, sub_str)
print(result) 
