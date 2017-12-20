user_input = 999
while user_input != "0":
    user_input = input("십진수 숫자를 입력해주세요 : ")
    try:
        decimal_number = int(user_input)
        print(bin(decimal_number))
    except ValueError as e:
        print(e)
        print("Error - 10진수 숫자만 입력해주시기 바랍니다.")

