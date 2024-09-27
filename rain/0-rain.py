#!/usr/bin/python3
"""Module for the rain function
"""
"""
This module provides a function to calculate the amount of rainwater trapped
between walls after it rains.
The walls are represented by non-negative integers
where each integer corresponds to the height of a wall of unit width.

Function:
    - rain(walls): Calculates and returns the total amount of water trapped.

Example:
    >>> rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    6
"""


def rain(walls):
    """
    Calculate how much rainwater can be trapped between walls after it rains.

    Args:
        walls (list): A list of non-negative integers representing the heights
                      of walls with unit width 1.

    Returns:
        int: The total amount of rainwater trapped (measured in square units).

    Assumptions:
        - If the list is empty or has fewer than 3 walls,
        no water can be trapped, so return 0.
        - The ends of the list are not considered walls,
        so no water is trapped beyond the first and last walls.

    Approach:
        - Precompute two arrays: left_max and right_max.
            - left_max[i] stores the highest wall to the left of or at index i.
            - right_max[i]
            stores the highest wall to the right of or at index i.
        - For each index i,
            calculate the water trapped as the difference between
          the minimum of left_max[i] and right_max[i],
          and the height of walls[i].
        - Accumulate the total water trapped at each index.

    Time Complexity: O(n), where n is the length of the input list.
    Space Complexity: O(n),
    due to the extra space used for the left_max and right_max arrays.

    Example:
        >>> rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        6

        Explanation:
        - Water is trapped between the walls at various points,
        leading to a total of 6 units of water.
    """

    if not walls or len(walls) < 3:
        return 0

    n = len(walls)

    # Initialize left_max and right_max arrays
    left_max = [0] * n
    right_max = [0] * n

    # Fill left_max array
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Fill right_max array
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate trapped water
    total_water = 0
    for i in range(n):
        total_water += min(left_max[i], right_max[i]) - walls[i]

    return total_water
