print("당신이 태어난 년도를 입력하세요")
birth_year = input()
age = 2017 - int(birth_year) + 1

if 20<= age <=26  :
    print("대학생")
elif  17 <= age < 20:
    print("고등학교")
elif  14 <= age < 17:
    print("중학생")
elif   8 <= age < 14 :
    print("초등학생")
else:
    print("학생이 아닙니다")
