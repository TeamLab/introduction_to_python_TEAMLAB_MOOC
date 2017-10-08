for i in range(10):
    try:
        print(i, 10 // i)
    except ZeroDivisionError:
        print("Not divided by 0")
