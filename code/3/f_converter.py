print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다")
print("변환하고 싶은 섭씨  온도를 입력해 주세요:")

user_input = input()
fah = ((9/5) * float(user_input) ) + 32

print("섭씨온도 :", user_input)
print("화씨온도 :", fah)
