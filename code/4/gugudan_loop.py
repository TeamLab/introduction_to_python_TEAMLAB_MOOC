print ("구구단 몇 단을 계산할까요(1~9)?")
x = 1
while (x is not 0):
    x = int(input())
    if x == 0: continue
    if not(1 <= x <= 9):
        print ("잘못 입력하셨습니다",
            "1부터 9사이 숫자를 입력해주세요")
        continue
    else:
        print ("구구단 " + str(x) +"단을 계산합니다.")
        for i in range(1,10):
            print (str(x) + " X " + str(i) + " = " + str(x*i))
        print ("구구단 몇 단을 계산할까요(1~9)?")
print ("구구단 게임을 종료합니다")
