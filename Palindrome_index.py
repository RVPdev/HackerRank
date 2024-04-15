# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# Define a function to check if a given string s is a palindrome
def is_palindrome(s):
    return s == s[::-1]  # Return True if the string reads the same forward and backward

# Define the main function to find the index at which removing a character could make the string a palindrome
def palindrome_index(s):
    if is_palindrome(s):  # First, check if the input string is already a palindrome
        return -1         # Return -1 if no removal is needed because the string is already a palindrome

    # Initialize pointers for the start and end of the string
    left, right = 0, len(s) - 1

    # Loop through the string from both ends towards the center
    while left < right:
        if s[left] != s[right]:  # Check if the characters at these positions are different
            # If removing the character at 'left' index makes it a palindrome, check it
            if is_palindrome(s[left + 1: right + 1]):
                return left       # Return the 'left' index if this substring is a palindrome
            # If removing the character at 'right' index makes it a palindrome, check it
            if is_palindrome(s[left: right]):
                return right      # Return the 'right' index if this substring is a palindrome
            break  # If neither removal results in a palindrome, break the loop

        # Move the pointers closer to the center
        left += 1
        right -= 1

    return -1  # Return -1 if no single removal can make the string a palindrome

# Example usage
print(palindrome_index("abca"))  # Output should be 1 because removing the character at index 1 makes it a palindrome
