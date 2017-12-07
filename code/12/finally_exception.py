for i in range(0, 10):
    try:
        result = 10 // i
        print(i, "------", result)
    except ZeroDivisionError:
        print("Not divided by 0")
    finally:
        print("종료되었습니다.")
