tuples_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_list = sorted(tuples_list, key=lambda x: x[-1])

print("Sorted List:", sorted_list)

# output
# Sorted List: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]