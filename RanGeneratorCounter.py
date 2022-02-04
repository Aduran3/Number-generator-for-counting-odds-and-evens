# Function for generating random integers and counting the evens and odds
#
# @author     Duran, Aaron
# 
# @date       10/10/2021
import random


# generates a random value
def get_random(a, b):
    if a >= b:
        generated = "INVALID RANGE"
    else:
        generated = random.randint(a, b)
    return generated


# tests if value is even
def is_even(a):
    return a % 2 == 0


print("This program serves to generate 100 random numbers of a desired range from A to B and")
print("counts how many generated values are even and how many are odd.")

while True:
    try:
        a = int(input("Enter A value: "))
        b = int(input("Enter B value: "))
        if b > a:
            break;
        else:
            print("Invalid range, ensure A is larger than B.")
    except ValueError:
        print("Invalid range, ensure the values are integers.")
        continue

print("Your 100 random numbers are:", end=" ")

runs = 0
odds = 0
evens = 0
while runs < 100:
    GenNumber = get_random(a, b)
    print(GenNumber, end=" ")
    if is_even(GenNumber) is True:
        evens += 1
    else:
        odds += 1
    runs += 1

print()
print("With", evens, "evens and", odds, "odds.")