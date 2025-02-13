# Problem 4: Print divisibility conditions for numbers 1-50
# by Medina Kubanychbekova
# Date: 02/12/2025
# Description: This program prints different messages based on divisibility by 3 and 5.

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Divisible by three")
    elif i % 5 == 0:
        print("Divisible by five")
    else:
        print(i)
