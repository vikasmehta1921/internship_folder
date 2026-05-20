# Question 2: String Concatenation and Methods Practice
# Input 2 strings, concatenate them and store in another variable.
# Then perform generally used string methods on it like:
# lower(), upper(), title(), swapcase(), capitalize(), casefold(), center(),
# count(), endswith(), find(), isalnum(), isdigit(), isnumeric(), isspace(), replace()

def main():
    print("=== String Methods Practice ===")
    
    # Input 2 strings
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    
    # Concatenate them
    combined_str = str1 + str2
    print(f"\nConcatenated String: '{combined_str}'")
    print("-" * 50)
    
    # Performing string methods
    print(f"1. lower()      : {combined_str.lower()}")
    print(f"2. upper()      : {combined_str.upper()}")
    print(f"3. title()      : {combined_str.title()}")
    print(f"4. swapcase()   : {combined_str.swapcase()}")
    print(f"5. capitalize() : {combined_str.capitalize()}")
    print(f"6. casefold()   : {combined_str.casefold()}")
    print(f"7. center(30)   : '{combined_str.center(30)}' (padded to 30 chars)")
    
    # Substring search practices
    sub_char = input("\nEnter a character/substring to count: ")
    print(f"8. count('{sub_char}')  : {combined_str.count(sub_char)}")
    
    end_char = input("Enter a suffix to check endswith(): ")
    print(f"9. endswith('{end_char}'): {combined_str.endswith(end_char)}")
    
    find_char = input("Enter a substring to find(): ")
    print(f"10. find('{find_char}')  : {combined_str.find(find_char)}")
    
    # Boolean checks
    print("\nBoolean String Checks:")
    print(f"11. isalnum()   : {combined_str.isalnum()}")
    print(f"12. isdigit()   : {combined_str.isdigit()}")
    print(f"13. isnumeric() : {combined_str.isnumeric()}")
    print(f"14. isspace()   : {combined_str.isspace()}")
    
    # Replacement
    old_val = input("\nEnter substring to replace: ")
    new_val = input("Enter replacement string: ")
    print(f"15. replace()   : {combined_str.replace(old_val, new_val)}")
    
    print("-" * 50)

if __name__ == "__main__":
    main()
