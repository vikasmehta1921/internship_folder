# Question 4: Assignment Operators Practice
# Do practice of assignment operators:
# =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=

def main():
    print("=== Assignment Operators Demonstration ===\n")
    
    # 1. Simple Assignment (=)
    x = 10
    print(f"Simple Assignment (=)       : x = {x}")
    
    # 2. Add and Assign (+=)
    x += 5
    print(f"Add and Assign (+= 5)        : x = {x} (same as x = x + 5)")
    
    # 3. Subtract and Assign (-=)
    x -= 3
    print(f"Subtract and Assign (-= 3)   : x = {x} (same as x = x - 3)")
    
    # 4. Multiply and Assign (*=)
    x *= 2
    print(f"Multiply and Assign (*= 2)   : x = {x} (same as x = x * 2)")
    
    # 5. Divide and Assign (/=)
    x /= 4
    print(f"Divide and Assign (/= 4)     : x = {x} (same as x = x / 4)")
    
    # 6. Modulus and Assign (%=)
    x %= 5
    print(f"Modulus and Assign (%= 5)    : x = {x} (same as x = x % 5)")
    
    # Resetting x for integer-specific demonstrations
    x = 15
    print(f"\n--- Resetting x to {x} for next operators ---")
    
    # 7. Floor Division and Assign (//=)
    x //= 2
    print(f"Floor Division (//= 2)       : x = {x} (same as x = x // 2)")
    
    # 8. Exponent and Assign (**=)
    x **= 3
    print(f"Exponent and Assign (**= 3)  : x = {x} (same as x = x ** 3)")
    
    # Resetting x for bitwise operations
    x = 5  # Binary: 0101
    print(f"\n--- Resetting x to {x} (Binary: 0101) for Bitwise Assignments ---")
    
    # 9. Bitwise AND and Assign (&=)
    x &= 3  # 3 is Binary: 0011. AND result: 0001 (1)
    print(f"Bitwise AND (&= 3)           : x = {x} (same as x = x & 3)")
    
    # 10. Bitwise OR and Assign (|=)
    x |= 2  # 2 is Binary: 0010. OR result: 0011 (3)
    print(f"Bitwise OR (|= 2)            : x = {x} (same as x = x | 2)")
    
    # 11. Bitwise XOR and Assign (^=)
    x ^= 1  # 1 is Binary: 0001. XOR result: 0010 (2)
    print(f"Bitwise XOR (^= 1)           : x = {x} (same as x = x ^ 1)")
    
    # 12. Bitwise Right Shift and Assign (>>=)
    x >>= 1  # Shift right by 1 bit: 0010 becomes 0001 (1)
    print(f"Right Shift (>>= 1)          : x = {x} (same as x = x >> 1)")
    
    # 13. Bitwise Left Shift and Assign (<<=)
    x <<= 2  # Shift left by 2 bits: 0001 becomes 0100 (4)
    print(f"Left Shift (<<= 2)           : x = {x} (same as x = x << 2)")

if __name__ == "__main__":
    main()
