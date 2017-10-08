def test(t):
	t = 20
	print ("In Function :", t)

x = 10
print ("Before :", x)   # 10
test(x)			# 함수 호출
print ("After :", x)	# 10 – 함수내부의 t는 새로운 주소값을 가짐
