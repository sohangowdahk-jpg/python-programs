# Search for an element in a list and stop when found
list = [1, 2, 3, 4, 5]
element_to_find = 3

for item in list:
    if item == element_to_find:
        print("Element found!")
        break
else:
    print("Element not found!")