import random			# 난수 발생 함수 호출
guess_number = random.randint(1, 100) 	# 1~100 사이 정수 난수 발생
print ("숫자를 맞춰보세요 (1 ~ 100)")
users_input = int(input())	     	# 사용자 입력을 받음
while (users_input is not guess_number):    	# 사용자 입력과 난수가 같은지 판단
    if users_input > guess_number: 	# 사용자 입력이 클 경우
        print ("숫자가 너무 큽니다")
    else: 		    		# 사용자 입력이 작은 경우
        print ("숫자가 너무 작습니다")
    users_input = int(input())	# 다시 사용자 입력을 받음
else:
    print ("정답입니다. ",
        "입력한 숫자는 ", users_input , "입니다")	# 종료 조건
