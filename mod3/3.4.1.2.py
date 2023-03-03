numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)

numbers[1] = numbers[4]
print("Previous list content:", numbers)

print("\nList's length", len(numbers))


del numbers[1]
print("New list's length:", len(numbers))
print("\nNew list content:", numbers)
