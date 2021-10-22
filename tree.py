picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

# print a space if 0 and print a * if a one, maintaining the same rows

for l in picture:
    for px in l:
        if px == 0:
            print(' ', end='')
        elif px == 1:
            print('*', end='')
    print(end='\n')