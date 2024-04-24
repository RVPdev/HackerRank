class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Convert each string to a list of characters. This allows easier manipulation of individual characters.
        arr1 = [x for x in word1]
        arr2 = [x for x in word2]

        # Initialize an empty string to build the result.
        result = ""

        # Continue looping as long as either arr1 or arr2 has elements left.
        while arr1 or arr2:
            # If arr1 still has characters, pop the first character from the front and append it to the result string.
            if arr1:
                ltr1 = arr1.pop(0)  # Pop the first element from arr1.
                result += ltr1       # Append the character to the result string.

            # Similarly, if arr2 still has characters, pop the first character from the front and append it to the result string.
            if arr2:
                ltr2 = arr2.pop(0)  # Pop the first element from arr2.
                result += ltr2       # Append the character to the result string.
        
        # Return the final merged string after all characters from both arrays have been appended.
        return result
