"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""


def median(n):
    if len(n) == 0:
        return 0
    if len(n) == 1:
        return n[0]

    n.sort()
    length = len(n)

    if length % 2 == 1:
        return n[int((length-1)/2)]
    elif length % 2 == 0:
        result = (n[int(length/2)] + n[int((length/2)-1)])/2
        return result


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median(numbers))
