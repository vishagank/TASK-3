def first_non_repeating_element(lst):
    # Create a dictionary to store the count of each element
    element_count = {}

    # First pass: count the occurrences of each element
    for num in lst:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    # Second pass: find the first element with a count of 1
    for num in lst:
        if element_count[num] == 1:
            return num

    # If no non-repeating element is found, return None or a message
    return None


# Test the function with a sample list
lst = [2, 3, 2, 4, 5, 3, 4]
print(first_non_repeating_element(lst))  # Output: 5
