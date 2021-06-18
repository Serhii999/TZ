for num in range(11, 80):
    if num % 3 == 0 and num % 5 == 0:
        print('$$@@')
    elif num % 3 == 0:
        print('$$')
    elif num % 5 == 0:
        print('@@')
    else:
        print(num)


