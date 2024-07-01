def is_happy_number(n):
    seen_numbers = set()
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum(int(digit)**2 for digit in str(n))  # Replace the number with the sum of the squares of its digits
    return n == 1  # Return True if n is 1 (happy), False otherwise

def count_happy_numbers(lst):
    happy_count = 0  # Initialize counter for happy numbers
    for number in lst:
        if is_happy_number(number):  # Check if the number is happy
            happy_count += 1  # Increment the counter if it is happy
    return happy_count  # Return the total count of happy numbers

# Example list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Count happy numbers in the list
happy_count = count_happy_numbers(numbers)
print(f"There are {happy_count} happy numbers in the list.")
