def flippingMatrix(matrix):
    # The length of the matrix is 2n, so n is half the length
    n = len(matrix) // 2
    max_sum = 0  # Initialize the sum of the top-left quadrant

    # Iterate over each cell in the top-left quadrant
    for i in range(n):
        for j in range(n):
            # For each cell in the top-left quadrant, we have four options to choose from:
            # 1. The current cell itself (matrix[i][j])
            # 2. The horizontally mirrored cell in the top-right quadrant (matrix[i][2*n-j-1])
            # 3. The vertically mirrored cell in the bottom-left quadrant (matrix[2*n-i-1][j])
            # 4. The diagonally opposite cell in the bottom-right quadrant (matrix[2*n-i-1][2*n-j-1])

            # We choose the maximum of these four options. This ensures that we are maximizing
            # the value in each cell of the top-left quadrant after the flipping operations.
            max_sum += max(
                matrix[i][j],  # Top-left
                matrix[i][2*n-j-1],  # Top-right
                matrix[2*n-i-1][j],  # Bottom-left
                matrix[2*n-i-1][2*n-j-1]  # Bottom-right
            )

    # Return the total sum of the maximized top-left quadrant
    return max_sum

# Example usage
matrix = [
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]
print(flippingMatrix(matrix))  # Output will be the maximized sum
