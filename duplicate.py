some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicate_values = []

# Take the duplicates objects and add them to a list without using a set
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicate_values:
            duplicate_values.append(value)
print(duplicate_values)