__author__ = 'Alec'

"""
Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.

Sample Dataset:
100 200

Sample Output:
7500

"""

a = int(raw_input("First number? "))
b = int(raw_input("Second number? "))

# list comprehension
lst = [x for x in range(a, b + 1) if (x % 2 == 1)]

print sum(lst)
