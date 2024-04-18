def findPairsWithDifference(arr, k):
    # Create a set from the array elements
    elements = set(arr)
    count = 0

    # Check for each element if there exists another element with the required difference
    for number in arr:
        if number + k in elements:
            count += 1
        # Uncomment the following line if pairs in both directions count separately
        # if number - k in elements:
        #     count += 1

    return count

# Example usage
arr = [1, 5, 3, 4, 2]
k = 2
print(findPairsWithDifference(arr, k))  # Output: 3