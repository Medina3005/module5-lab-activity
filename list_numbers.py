# Problem 2: Print numbers and their squares
# by Medina Kubanychbekova
# Date: 02/12/2025
# Description: This program prints each number in a list and its square.

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Part a: Print each number
print("Numbers in the list:")
for num in numbers:
    print(num)

# Part b: Print each number and its square
print("\nNumbers and their squares:")
for num in numbers:
    print(f"{num} squared is {num**2}")
