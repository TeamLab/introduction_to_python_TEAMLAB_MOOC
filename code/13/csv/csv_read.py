line_counter = 0	#파일의 총 줄수를 세는 변수
data_header = []	#data의 필드값을 저장하는 list
customer_list = []	#cutomer 개별 List를 저장하는 List

with open ("customers.csv") as customer_data: #customer.csv 파일을 customer_data 객체에 저장

    while 1:
        data = customer_data.readline() #customer.csv에 한줄씩 data 변수에 저장
        if not data: break	 #데이터가 없을 때, Loop 종료
        if line_counter==0: 	 #첫번째 데이터는 데이터의 필드
            data_header = data.split(",") 	#데이터의 필드는 data_header List에 저장, 데이터 저장시 “,”로 분리
        else:
            customer_list.append(data.split(",")) #일반 데이터는 customer_list 객체에 저장, 데이터 저장시 “,”로 분리
        line_counter += 1

print("Header :\t", data_header)	#데이터 필드 값 출력
for i in range(0,10):		 #데이터 출력 (샘플 10개만)
    print ("Data",i,":\t\t",customer_list[i])
print (len(customer_list))		 #전체 데이터 크기 출력
