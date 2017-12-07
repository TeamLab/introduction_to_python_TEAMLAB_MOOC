#난수
import random
print (random.randint (0,100)) # 0~100사이의 정수 난수를 생성
print (random.random())  # 일반적인 난수 생성

#시간
import time
print(time.localtime()) # 현재 시간 출력

#웹
import urllib.request
response = urllib.request.urlopen("http://cs50.gachon.ac.kr")
print(response.read())

