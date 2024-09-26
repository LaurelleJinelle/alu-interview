def rain(walls):
  """Function to find the maximum rain collected
    by a series of walls
    """
    if not walls:
        return 0

    n = len(walls)
    
    # Initialize left_max and right_max arrays
    left_max = [0] * n
    right_max = [0] * n

    # Find the highest wall to the left of each element
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Find the highest wall to the right of each
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate trapped water
    total_water = 0
    for i in range(n):
        total_water += min(left_max[i], right_max[i]) - walls[i]

    return total_water
