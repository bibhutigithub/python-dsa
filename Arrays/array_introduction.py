# Simple example of array declaration and linear search.
my_arr = [10, 12, 25, 35]
item_to_search = 25
for idx, elem in enumerate(my_arr):
    if elem == 25:
        print("Item found at position: ", idx)
