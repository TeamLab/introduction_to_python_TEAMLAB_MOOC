Extreme Lab #2 - 주식 데이터 마음대로 모으기 (Stock Data Crawler Advance)
=========================================================================

Copyright 2015 © document created by TeamLab.Gachon@gmail.com

Introduction
------------

Stock Data Crawler를 성공적으로 끝낸 여러분들에게 이제 주식 정보를 긁어오는 건 정말 쉬운 일이 됐을 것입니다. 그래서 준비했습니다. 이번 Lab의 목적은 긁어오는 데이터의 회사와 범위를 실행 시점에서 정하는 것입니다. 사실 많이 복잡해보이지만 실제로는 그렇지 않습니다. 조금만 알면 비교적 쉽게 실행할 수 있습니다.

Stock Data Advance Overview
---------------------------

본 Lab이 기존 Stock Data Crawler랑 다른 점 두 가지입니다.

1) 사용자 입력에 의해 CSV 파일의 다운로드 URL이 바뀐다. 2) 사용자 입력이 형태가 바뀐다. ex) ALL-005930.KS-2014/12/01-2015/12/30

즉 사용자의 바뀐 입력 형태를 분석하여, CSV 파일을 다운로드 하고 이를 화면에 보여주거나, 파일에 저장하는 것입니다.

이미 설명했지만 우리가 다운로드 할 데이터의 URL 예시는 다음과 같습니다.

> http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2013&g=d

위 주소의 Base 주소는 `http://real-chart.finance.yahoo.com/table.csv`이며 그 뒤로 나오는 `s`, `a`, `b` 등의 값에 입력에 따라 다양한 주식 정보 데이터를 다운로드 받을 수 있습니다. 설정할 수 있는 값은 아래와 같습니다.

| 키 | 설명       | 값                | 비고                         |
|----|------------|-------------------|------------------------------|
| s  | 종목(심볼) | 005930.KS         | Samsung Electronics Co. Ltd. |
| a  | 시작 월    | 0                 | 1월 (0부터 시작)             |
| b  | 시작 일    | 1                 |                              |
| c  | 시작 년    | 2013              |                              |
| d  | 끝 월      | 11                | 12월 (0부터 시작)            |
| e  | 끝 일      | 31                |                              |
| f  | 끝 년      | 2013              |                              |
| g  | 기간       | d:일, w :주, m:월 | v:'배당'만 표시              |

위의 값을 자유롭게 바꾸면 다양한 주식 정보를 구할 수 있습니다. 예를 들면, `s=005380.KS`를 입력하고 `d=11&e=31&f=2015`로 입력한다면 현대 자동차의 2015년 12월 31일까지의 주식정보를 다운로드 받을 수 있습니다.

기업들은 아래와 같이 다양한 기업들을 선택할 수 있고, 기업코드만 안다면 우리나라 전체 기업의 주식 정보를 기간을 정해서 다운로드 받을 수 있습니다.

| 종목 심볼 | 종목명     | 종목 심볼 | 종목명       |
|-----------|------------|-----------|--------------|
| 005930.KS | 삼성전자   | 032830.KS | 삼성생명     |
| 005380.KS | 현대차     | 051910.KS | LG화학       |
| 005490.KS | POSCO      | 009540.KS | 현대중공업   |
| 012330.KS | 현대모비스 | 017670.KS | SK텔레콤     |
| 000660.KS | SK하이닉스 | 105560.KS | KB금융       |
| 035420.KS | NAVER      | 096770.KS | SK이노베이션 |
| 005935.KS | 삼성전자우 | 023530.KS | 롯데쇼핑     |
| 015760.KS | 한국전력   | 086790.KS | 하나금융지주 |
| 055550.KS | 신한지주   | 000810.KS | 삼성화재     |
| 000270.KS | 기아차     | 066570.KS | LG전자       |

이러한 URL 코드를 동적으로 만들기 위해 main 함수에서 입력하는 명령이 다음과 같이 바뀝니다.

> ALL-005930.KS-2014/12/01-2015/12/30 명령어-주식코드-시작년/월/일-종료년/월/일
>
> Open-005930.KS-2014/12/01-2015/12/30-example.csv 명령어-주식코드-시작년/월/일-종료년/월/일-저장하고자 하는 파일명

첫 번째 명령어는 ALL 또는 CSV 데이터의 Header 값이 들어갈 수 있으며, 맨 마지막에는 파일명을 입력하면 결과 값이 파일에 저장되고, 파일명이 적혀있지 않다면 결과값이 화면에 출력됩니다.

숙제 template 파일 다운로드
---------------------------

먼저 숙제 template 파일을 다운받아야 합니다. Chrome 또는 익스플로러와 같은 웹 브라우저 주소창에 아래 주소를 입력합니다.

> https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_ex_2/lab_ex_2.zip

다운로드를 위해 View Raw 또는 Download 버튼을 클릭합니다. 또는 [Lab ex 2 - 다운로드 링크](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_ex_2/lab_ex_2.zip)를 클릭하면 자동으로 다운로드가 됩니다. 다운로드 된 lab_ex_2.zip 파일을 작업 폴더로 이동한 후 압축해제 후 작업하길 바랍니다.

stock_data_advance.py 파일 Overview
-----------------------------------

`atom editor`로 `stock_data_advance.py`을 열어 전체적인 개요를 봅니다. `atom stock_data_advance.py`명령으로 파일을 열어보면 `main` 함수와 여러개의 함수들이 존재할 것입니다. 각 함수들은 여러분께서 직접 작성해서 제출해야 하는 함수이고, `main` 함수는 실제 주식 정보를 요청하여 프로그램을 실행하는 함수입니다. 각 함수의 구현 내용은 아래와 같습니다.

| 함수                     | 설명                                                                                                                                                                                                                                                                                                                                              |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| is_validate_url          | 입력변수인 url_address를 Yahoo 서버에 요청하면 해당 url_address가 사용이 가능한지에 대해 확인하는 Helper Function, 따로 수정할 필요는 없음                                                                                                                                                                                                        |
| is_validate_date         | 문자열로 yyyy/mm/dd의 형태로된 날짜 정보를 입력받아 조건에 맞는 경우 True, 그렇지 않을 경우 False를 반환함, <br> 1) 입력된 데이터를 "/"를 구분자로 나눴을 경우, 길이가 3이어야 함 <br>2) yyyy: 년도는 2001년 부터 2015년까지 입력됨 <br>3) mm: 월(month)정보는 1월 부터 12월까지 입력됨 4) dd: 일(day)는 1일 부터 31일 까지 입력됨(월에 상관없음) |
| is_validate_command      | 사용자의 입력값과 stock_data의 header 값을 입력받아 사용자의 입력값이 처리가능할 경우 True, 그렇지 않을 경우 False를 반환함 (하단 참조)                                                                                                                                                                                                           |
| make_stock_data_url      | yahoo finance의 csv 다운로드 입력 url를 입력된 7개의 변수를 바탕으로 생성함 <br> base_url은 "http://real-chart.finance.yahoo.com/table.csv?" 이며, 차례로 입력변수로 최종 주소를 만듦                                                                                                                                                             |
| get_stock_data           | url_address를 Input 변수로 넣으면 Yahoo 서버에 요청하면 해당 정보를 다운로드 받은 후 Two Dimensional List 변환하여 반환함, Two Dimenstional List에는 0번째 index의 Header Field list가, 다음 index부터는 데이터가 일별로 list가 들어가 있음                                                                                                       |
| get_header_data          | get_stock_data 함수의 반환값을 Input 변수로 넣으면 Header Field에 해당하는 값만 추출하여 list로 반환함                                                                                                                                                                                                                                            |
| get_attribute_data       | get_stock_data 함수의 Return 값, 추출하고자 하는 Header Field의 이름을 입력받으면 Date Field와 해당 조건의 값만 추출하여 list로 반환함                                                                                                                                                                                                            |
| write_csv_file_by_result | get_stock_data 함수의 반환값 또는 get_attribute_data 함수의 반환값, 생성하고자 하는 파일 이름을 String Type의 Input 변수로 넣으면, 입력된 List 값이 들어있는 파일을 생성함                                                                                                                                                                        |
| separate_user_query      | 사용자의 입력 값을 "-" 기준으로 나눠 list로 반환하며 반드시 각 list에 값들은 빈칸이 제거된 후 저장되어야 함                                                                                                                                                                                                                                       |

개별 함수 설명
--------------

Stock Data Crawler 함수와 마찬가지로 이번 랩은 추가 설명이 꽤 필요하기 때문에 필요한 함수들에 대해서 추가 설명을 합니다. 단, Stock Data Crawler에서 이미 설명한 함수는 제외합니다.

> make_stock_data_url

make_stock_data_url은 7개의 입력 변수를 받아 하나의 URL 주소를 만듭니다. String Type의 데이터를 붙이는 가장 간단한 방법은 "+" 기호를 사용하는 것이지만, 아래와 같이 string formatting을 이용하는 것이 좋습니다.

```python
>>> a = "Hello, {0}".format("World")
>>> a
'Hello, World'
```

string formatting은 string를 연결하기 위해 가장 쉬운 방법 중 하나로 따옴표 안에 {0}, {1}, {2} 와 같은 기호와 숫자를 쓰고 format 함수안에 tuple 형태의 데이터를 차뎨로 쓰면 tuple index 기호에 해당하는 숫자들이 string 안으로 대입되게 됩니다. 이것을 사용하면 비교적 쉽게 url을 생성할 수 있습니다.\`\` > is_validate_command

사용자의 입력을 받았을 때 아래 조건을 만족하면 True, 만족하지 않으면 False를 반환합니다.

1) 유저의 입력값은 "-"으로 나눠짐 2) 유저의 입력값의 예제는 아래와 같으며 각각 다음과 같은 의미를 가짐

ALL-005930.KS-2014/12/01-2015/12/30 명령어-주식코드-시작년/월/일-종료년/월/일 ALL-005930.KS-2014/12/01-2015/12/30-example.csv 명령어-주식코드-시작년/월/일-종료년/월/일-저장하고자 하는 파일명

3) 입력 변수 command_str를 "-" 나눴을 경우 길이는 4 또는 5이여야 함 4) command_str를 "-"으로 나눴을 경우, 0번째 Index의 값은 ALL또는 header_field에 있는 값이어야 함, 또한 대소문자는 구분하지 않아야 함 5) command_str를 "-"으로 나눴을 경우, 2,3번째 is_validate_date에 입력시 True를 반환해야 함 6) command_str를 "-"으로 나눴을 경우, 1,2,3번째의 값으로 yahoo 금융서버에 접속하는 url을 생성한 후, is_validate_url에 입력시 True를 반환해야 함

한 가지 차이점이 있다면, 기존 Stock Data Crawler는 첫번째 명령어의 대소문자를 구분하였지만, 본 Lab에서는 구분하지 않습니다.

main 함수 수정하기
------------------

위의 함수들을 작성하고 나면 `main`함수를 수정해야 합니다. `main`함수의 기본 template은 아래와 같습니다.

```python
def main():
    print("Stock Data Crawler Program!!")
    user_input = 999
    # ===Modify codes below=============

    # ==================================
```

`main` 함수는 다음과 같은 규칙을 가집니다.

1.	사용자가 0을 입력하면 종료된다.
2.	사용자의 입력값이 is_validate_command에 입력되어 False를 반환하면 "Wrong Input, Please, Input"을 출력한다.
3.	사용자의 입력값의 맨 끝에 파일명이 있으면 해당 파일을 생성한다.
4.	사용자의 입력값의 맨 끝에 파일명이 없으면 stock data를 화면에 출력한다.
5.	사용자의 입력값의 첫 번째 값인 명령어가 ALL이면 모든 데이터를, 특정 Header Field 이름이라면 해당 Field의 값만 보여준다(또는 저장한다).

실제로 작성된 프로그램의 실행화면은 다음과 같습니다.

![Stock Data Advance 실행화면 1](https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/ex_lab_2_stock_data_advance/stock_data_advance_screenshot.png)

숙제 제출하기
-------------

모든 함수를 다 수정했다면, 아래와 같이 제출해봅시다.

-	`windows`\+`r`를 누르고 cmd 입력 후 확인을 클릭합니다.
-	작업폴더로 경로를 이동합니다.
-	cmd 창에서 아래의 코드를 입력합니다.

```bash
python submit.py
```

위 명령어를 입력하면, 아래와 같은 내용이 띄면서 Login ID와 Password를 물어봅니다. http://theteamlab.io 웹 페이지에 가입시 사용했던 email 주소와 비밀번호를 입력합니다.

```bash
== Submmting solutions | arithmetic_function.py
Login ID:
Password :
```

제대로 작성했다면 아래와 같은 메세지가 뜰 것입니다. 마찬가지로 실행시 오랜 시간이 걸립니다. 그 이유는 코드를 테스트 하는 프로그램이 내부적으로 데이터를 다운로드 받고 하는 파일로 만드는 시간이 있기 때문입니다. 조금 기다려서 실행하면 결과가 나오니 중간에 끄거나 하지 맙시다.

```bash
------------------------ | ---------- | --------------------
       Function Name     |    Passed? |             Feedback
------------------------ | ---------- | --------------------
    is_validate_date     |       PASS |             Good Job
 separate_user_query     |       PASS |             Good Job
 make_stock_data_url     |       PASS |             Good Job
     get_header_data     |       PASS |             Good Job
 is_validate_command     |       PASS |             Good Job
write_csv_file_by_result |       PASS |             Good Job
  get_attribute_data     |       PASS |             Good Job
      get_stock_data     |       PASS |             Good Job
                main     |       PASS |             Good Job
------------------------ | ---------- | --------------------
```

Next Work
---------

수고하셨습니다.

> **Human knowledge belongs to the world** - from movie 'Password' -

Footnotes
---------
