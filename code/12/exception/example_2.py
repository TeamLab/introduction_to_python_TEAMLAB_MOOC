for i in range(10):
    try:
        print(i, 10 // i)
    except ZeroDivisionError as err:
        print(err)
        print("Not divided by 0")
