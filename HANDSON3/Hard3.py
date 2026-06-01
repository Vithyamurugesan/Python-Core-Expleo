def findMax(*numbers):

    maximum = numbers[0]

    for i in numbers:
        if i > maximum:
            maximum = i

    return maximum

print("Maximum value among four integers:",
      findMax(25, 12, 18, 30))

print("Maximum value among five integers:",
      findMax(8, 15, 22, 17, 12))