Lab #11 - File IO Example (file_io_example)
=======
Copyright 2015 © document created by TeamLab.Gachon@gmail.com

## Introduction
이번 Lab은 쉽다. 다행이다. 쉽다. 즐겁지 않은가? 쉽다.
이번 Lab은 Text Handling 시리즈의 첫 번째 Lab이다. 이번 Lab의 목표는 간단한 파일을 다운로드 받고, 파일안에 있는 정보를 추출하는 것 이다. 다행이다. 진짜 쉽다. 함수도 5개 밖에 없다. 바로 본론으로 들어가자.

## 숙제 template 파일 다운로드
먼저 숙제 template 파일을 cs50 서버로 부터 다운로드 받는다. 로그인 후 나타나는 `bash shell`에서 다음과 같은 명령을 입력하자. 이것부터 쉽게 느껴지지 않는가?

```bash
python3.4 submit_assignment.py -get file_io_example
```  

입력되면 다운로드 안내 메세지와 함께 `file_io_example.py` 파일이 다운로드 된다.

다음으로 이번 Lab에서 사용할 예제 파일을 다운로드 하자. 아래와 같이 bash shell에서 입력하면 된다.

```bash
wget https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_11_file_handling/1984.txt
```  



## file_io_example.py 파일 Overview
`vim editor`로 `file_io_example.py`을 열어 전체적인 개요를 보자. 이번 Lab은 오직 5개의 함수로만 구성되어 있으며, Main 함수는 존재하지 않는다.

이제 수정해야 할 함수 리스트를 보자

함수           | 설명 
--------       | ---
get_file_contents | 문자열값으로 filename을 입력받아 해당 파일에 존재하는 모든 text 데이터를 문자열 형태로 반환함 
get_number_of_characters_with_blank | 문자열값으로 filename을 입력받아 해당 파일에 존재하는 모든 글자의 갯수를 integer 값으로 반환함 
get_number_of_characters_without_blank | 문자열값으로 filename을 입력받아 해당 파일에 존재하는 모든 글자의 갯수를 공백을 제외하고 integer 값으로 반환함. 단 여기서 공백은 " ", "\t", "\n" 을 의미함
get_number_of_lines | 문자열값으로 filename을 입력받아 해당 파일에 존재하는 모든 줄(line)수를  integer 값으로 반환함. 이때 마지막 줄은 count에서 제외함
get_number_of_target_words | 문자열값으로 filename과 찾고자하는 target_words을 입력받아 해당 파일에 존재하는 target_words와 같은 글자의 수를 대소문자와 상관없이 integer 값으로 반환함 


## 결과확인
너무 쉽다. bash shell에서 test 한다면 다음과 같은 결과가  나올 것이다.

```bash
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import file_io_example as fie
>>> fie.get_file_contents("1984.txt").split("\n")[0]
'GEORGE ORWELL'
>>> fie.get_number_of_characters_with_blank("1984.txt")
558840
>>> fie.get_number_of_characters_without_blank("1984.txt")
459038
>>> fie.get_number_of_lines("1984.txt")
1414
>>> fie.get_number_of_target_words("1984.txt", "Hi")
3938
>>> fie.get_number_of_target_words("1984.txt", "had")
1327
>>> exit()
```

## 숙제 제출하기
모든 함수를 다 수정했다면, 아래와 같이 제출하자
```bash
 python3.4 submit_assignment.py -submit file_io_example.py
```  
제대로 작성했다면 아래와 같은 메세지가 뜰 것이다.
```bash
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
 get_number_of_lines |       PASS |             Good Job
   get_file_contents |       PASS |             Good Job
get_number_of_characters_with_blank |       PASS |             Good Job
get_number_of_characters_without_blank |       PASS |             Good Job
get_number_of_target_words |       PASS |             Good Job
-------------------- | ---------- | --------------------
```  

## Next Work
이번 랩은 너무 쉬우서 아마도 수업시간에 집에 하고 가는 사람이 많을 거 같다. 걱정말자 아직도 우리에겐 Text 분석 까지 3개의 Lab이 남았다. 3개의 Lab만 끝나면 놀수 있다. 좋지 아니한가?

> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes
