number = int(input("Enter the number:"))

last_digit = number % 10  # we can find the last number

while number >10:
    number = number // 10


print("The first int is" ,number ,"and the last int is",last_digit)


