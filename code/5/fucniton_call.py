def spam(eggs):
    eggs.append(1)  # 기존 객체의 주소값에 [1] 추가
    eggs = [2, 3]  # 새로운 객체 생성

ham = [0]
spam(ham)
print(ham)  # [0, 1]
