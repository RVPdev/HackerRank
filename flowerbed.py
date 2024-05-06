def canPlaceFlowers(flowerbed, n):
    count = 0  # Number of new flowers planted
    length = len(flowerbed)
    
    for i in range(length):
        # Check if the current plot is empty
        if flowerbed[i] == 0:
            # Check the previous and next plot (handle edge cases)
            prev_empty = (i == 0 or flowerbed[i - 1] == 0)
            next_empty = (i == length - 1 or flowerbed[i + 1] == 0)
            
            # If both conditions are satisfied, plant a flower
            if prev_empty and next_empty:
                flowerbed[i] = 1  # Plant the flower
                count += 1  # Increment the count of flowers planted
                
                # If we've planted enough flowers, return true
                if count >= n:
                    return True
    
    # If we exit the loop without having planted enough flowers
    return count >= n # can be replaced with FALSE
