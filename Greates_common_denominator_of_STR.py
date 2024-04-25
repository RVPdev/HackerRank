def gcdOfStrings(str1, str2):
    # Helper function to find the GCD of two numbers using the Euclidean algorithm.
    # This function computes the greatest common divisor of two numbers a and b.
    def gcd(a, b):
        # Continue looping until the remainder b becomes zero.
        while b:
            # Update a to be b, and b to be the remainder of a divided by b.
            a, b = b, a % b
        # When b is zero, a is the GCD of the original pair of numbers.
        return a
    
    # Check if a string x can be the common divisor of str1 and str2.
    # This function checks if string x can be repeatedly concatenated to form both str1 and str2.
    def check(x):
        # First, check if the length of x is a divisor of the lengths of both str1 and str2.
        if len(str1) % len(x) == 0 and len(str2) % len(x) == 0:
            # If x can be multiplied to match the length of str1 and does form str1,
            # and similarly for str2, then x is a valid common divisor.
            if x * (len(str1) // len(x)) == str1 and x * (len(str2) // len(x)) == str2:
                return True
        # If either condition fails, return False indicating x cannot form both strings.
        return False

    # Calculate GCD of the lengths of str1 and str2 using the gcd helper function.
    # This gcd value is used to determine the length of the potential greatest common divisor string.
    gcd_length = gcd(len(str1), len(str2))
    
    # The candidate for the greatest common divisor string is the substring of str1
    # from the beginning to the gcd length. This substring is the longest possible
    # string that could be a divisor of both strings.
    candidate = str1[:gcd_length]

    # Use the check function to see if the candidate can actually form both strings
    # by repeated concatenation.
    if check(candidate):
        # If the candidate works, return it as the greatest common divisor string.
        return candidate
    else:
        # If the candidate does not work, return an empty string indicating no
        # string can be the divisor.
        return ""
