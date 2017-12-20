try:
    for i in range(1, 10):
        result = 10 // i
        print(i, "------", result)
except ZeroDivisionError:
    print("Not divided by 0")
finally:
    print("종료되었습니다.")
