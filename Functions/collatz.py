def collatz():
    print('Please enter a number:')
    theinput = int(input())

    while theinput != 1:
        if theinput % 2 == 0:
            theinput = theinput // 2
            print(theinput)
        else:
            theinput = 3 * theinput + 1
            print(theinput)

collatz()