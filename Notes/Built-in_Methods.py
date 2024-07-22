# applicable to all data types including custom

#.len()
#.sum()
#.max()
#.min()
#.sorted() creates a new sorted list
original_list = [3, 1, 4, 2, 5]

# Sort the list in ascending order (default)
sorted_list = sorted(original_list)
print(original_list)  # Output: [3, 1, 4, 2, 5] (unchanged)
print(sorted_list)   # Output: [1, 2, 3, 4, 5]

# Sort by the length of strings (assuming original_list contains strings)
sorted_by_length = sorted(original_list, key=len)
print(sorted_by_length)  # Output: (sorted based on string lengths)

# Sort in descending order
sorted_descending = sorted(original_list, reverse=True)
print(sorted_descending)  # Output: [5, 4, 3, 2, 1]
