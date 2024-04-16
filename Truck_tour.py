def truckTour(petrolpumps):
    total_surplus = 0
    current_surplus = 0
    start_index = 0

    for i in range(len(petrolpumps)):
        petrol, distance = petrolpumps[i]
        total_surplus += petrol - distance
        current_surplus += petrol - distance
        
        # If surplus is negative, reset the start position
        if current_surplus < 0:
            start_index = i + 1
            current_surplus = 0
    
    # If total surplus is positive or zero, the tour can be completed
    if total_surplus >= 0:
        return start_index
    else:
        return -1  # This case is typically not needed given the problem constraints

# Example usage:
print(truckTour([(4, 6), (6, 5), (7, 3), (4, 5)]))  # Output: 1
