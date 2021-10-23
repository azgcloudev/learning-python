#create a function that prints the highes even number of the list
def highest_even(list):
    answer = 0
    for value in list:
        if value % 2 == 0:
            if value > answer:
                answer = value
    return answer

print(highest_even([10,2,3,4,8,11]))

# Other way to code this:
def highest_even2(li):
    evens = []
    for items in li:
        if items % 2 == 0:
            evens.append(items)
    return max(evens)

print(highest_even2([1,5,3,2,6,7,23,44,88,67,100]))