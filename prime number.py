# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

number_list = [10, 501, 22, 37, 100, 999, 87, 351]

# List to store prime numbers
prime_list = []

# Count the prime numbers and add them to the prime_list
for number in number_list:
    if is_prime(number):
        prime_list.append(number)

# Print the count of prime numbers
print("Count of prime numbers:", len(prime_list))

# Print the list of prime numbers
print("List of prime numbers:", prime_list)





