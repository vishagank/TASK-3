def find_duplicates(lst):
    # Create an empty list to store duplicates
    duplicates = []

    # Iterate over each element in the list
    for i in range(len(lst)):
        # Check if the element has already appeared in the list before
        if lst[i] in lst[:i]:
            # If the element is not already in duplicates, add it
            if lst[i] not in duplicates:
                duplicates.append(lst[i])

    return duplicates


# Test the function with a sample list
lst = [2, 3, 2, 4, 5, 3, 4, 6, 7, 7, 8]
print("the duplicates are:",find_duplicates(lst))