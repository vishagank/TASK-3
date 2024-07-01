def has_zero_sum_sublist(lst):
    # Create an empty set to store the sums we encounter
    seen_sums = set()

    # Start with a cumulative sum of 0
    current_sum = 0

    # Iterate over each element in the list
    for num in lst:
        # Add the current number to the cumulative sum
        current_sum += num

        # Check if the cumulative sum is zero or if it has been seen before
        if current_sum == 0 or current_sum in seen_sums:
            return True

        # Add the current sum to the set of seen sums
        seen_sums.add(current_sum)


    return False


# Test the function with the given list
lst = [4, 2, -3, 1, 6]
print(has_zero_sum_sublist(lst))  # Output: True
