Lab #4 - 화씨 변환기 (fahrenheit_converter)
=======
Copyright 2015 © document created by TeamLab.Gachon@gmail.com

## Introduction
5주차 강의 Lab Assignment 입니다. 이번 lab은 더 짧고 더 불친절합니다. 이번 랩은 이미 수업시간에 한번 다룬 화씨 변환기를 숙제 형식에 맞게 수정하였습니다. 이번 lab의 가장 큰 특징은 `main` 함수마저 수강생들이 직접 작성한다는 것입니다. 조금 어려워 보일수도 있으나 막상 끝나고 보면 쉬울 것입니다. 이번 lab에서는 개별 함수의 작성 그리고 각 함수들의 연결을 연습해 봅시다.

[PDF 파일 다운로드](https://github.com/TeamLab/introduction_to_python_TEAMLAB_MOOC/raw/master/lab_assignment/lab_4/lab_4.pdf)

## backend.ai 설치
숙제를 제출하기 앞서, [레블업](http://www.lablup.com/)의 backend.ai를 여러분의 파이썬에 설치하셔야 합니다. 설치하는 과정은 매우 쉽습니다. 아래처럼 터미널 또는 cmd 창에서 입력을 하시면 됩니다.

```bash
pip install backend.ai-client
```

## 숙제 파일(lab_4.zip) 다운로드
먼저 해야 할 일은 숙제 파일을 다운로드 받는 것 입니다. 이미 해보았기 때문에 어렵지 않을 것입니다. Chrome 또는 익스플로러와 같은 웹 브라우저 주소창에 아래 주소를 입력합니다.

[https://github.com/TeamLab/introduction_to_python_TEAMLAB_MOOC/blob/master/lab_assignment/lab_4/lab_4.zip](https://github.com/TeamLab/introduction_to_python_TEAMLAB_MOOC/blob/master/lab_assignment/lab_4/lab_4.zip)

다운로드를 위해 `View Raw` 또는 `Download` 버튼을 클릭합니다. 또는 아래 다운로드 링크를 클릭하면 자동으로 다운로드가 됩니다. [Lab 4 - 다운로드](https://github.com/TeamLab/introduction_to_python_TEAMLAB_MOOC/raw/master/lab_assignment/lab_4/lab_4.zip)
다운로드 된 lab_4.zip 파일을 작업 폴더로 이동한 후 압축해제 후 작업하길 바랍니다.
압축해제 하면 폴더가 `linux_mac`과 `windows`로 나눠져 있습니다. 자신의 OS에 맞는 폴더로 이동해서 코드를 수정해 주시기 바랍니다.

## fahrenheit_converter.py 파일 Overview
`atom`으로 `fahrenheit_converter.py`을 열어 전체적인 개요를 봅시다. 파일을 열어보면 아래와 같은 내용이 파일에 기록되어 있을 것입니다.

```python
# -*- coding: utf-8 -*-


def main():
    print("본 프로그램은 섭씨를 화씨로로 변환해주는 프로그램입니다")
    print("============================")
    # ===Modify codes below=================

    # ======================================
    print("===========================")
    print("프로그램이 종료 되었습니다.")


if __name__ == '__main__':
    main()
```

수강생이 할일은 크게 두 가지입니다. 하나는 프로그램 수행을 위해 3개의 함수를 작성하는 것이고, 두 번째는 `main`함수에 작성된 3개의 함수를 사용해서 화씨 변환기를 돌려 보는 것입니다. 현재 코드는 헐렁하지만 여러분들이 빈 공간을 채우면 됩니다.

## input_celsius_value 함수 작성하기
3개의 함수 부터 작성해봅시다. 이미 함수 하나를 작성하는 것은 lab 3에서 연습해보았기 때문에 어렵지 않을 수도 있습니다. 아래 내용을 참고하여 `input_celsius_value` 함수를 작성해봅시다.

내용           | 구성
--------       | ---
함수명      | input_celsius_value
input 변수(argument) | 없음
Process  | "변환하고 싶은 섭씨  온도를 입력해 주세요: " 이라는 글자를 화면에 출력하고, 입력된 값을 실수로 변환해줍니다. 사용자는 실수값 형태로만 입력한다고 가정합니다.
output 값(return value)  | Float Type의 celsius_value

함수를 작성하고 나서 잘 작동하는 지 궁금할 것입니다. 확인하는 방법은 두가지가 있습니다. 먼저 아래처럼 기존 코드에서 `main` 함수를 주석 처리하고 테스트 코드를 삽입하는 방법입니다. `fahrenheit_converter.py` 파일을 `atom`으로 열어 맨 마지막 `if __name__ == '__main__':`을 아래처럼 수정해 봅시다.

```python
if __name__ == '__main__':
    # main()
    celsius_value = input_celsius_value()
    print(celsius_value)
```

함수가 정상적으로 작성된 후, `cmd` 창에서 `python fahrenheit_converter.py`을 실행하면 아래와 같은 화면을 보게 될 것입니다.

```bash
변환하고 싶은 섭씨  온도를 입력해 주세요: 15.2
15.2
```

입력해 준 값을 그대로 출력해 주는 것으로 별다른 특징은 없습니다.
코드 자체를 수정하여 테스트 코드를 넣는 방법도 있지만, 기존 처럼 `python shell`에서 테스트하는 방법도 있습니다. `cmd` 창에서 `python`을 입력하여 `python shell`을 실행 시켜서 아래와 같이 테스트 해봅시다.

```python
>>> import fahrenheit_converter as fc
>>> fc.input_celsius_value()
변환하고 싶은 섭씨  온도를 입력해 주세요:10
10.0
```

이미 `python shell`에서 테스트 하는 방법과 `import`문의 의미는 설명해 주었습니다. 더 이상의 자세한 설명은 생략합니다.

## convert_celsius_fahrenheit 함수 작성하기
두 번째 함수입니다. 두 번째 함수는 입력받은 float type의 섭씨 값을 화씨로 변환해 주는 함수입니다. 함수의 내용은 아래와 같습니다.

내용           | 구성
--------       | ---
함수명      | convert_celsius_fahrenheit
input 변수(argument)  | float type의 celsius_value
Process  | 섭씨=> 화씨의 변환 공식에 따라 섭씨를 화씨 값으로 변환해줍니다. 변환 공식은 `((9 / 5) * 섭씨값) + 32` 입니다. 여기서 `섭씨값` 특정한 변수명으로 변경되야 합니다. 기억하세요.
output 값(return value)    | Float Type의 섭씨값이 화씨값으로 변한된 값

테스트 코드는 이미 수업시간 다뤄 졌지만 `python shell` 수행시 아래와 같이 나오면 정상적으로 작성된 것입니다.
```python
>>> import fahrenheit_converter as fc
>>> fc.convert_celsius_fahrenheit(32.2)
89.96000000000001
>>> fc.convert_celsius_fahrenheit(50)
122.0
>>>
```
위에처럼 `if __name__ == '__main__':` 부분을 수정하여 테스트 코드를 만드는 일은 직접 해 봅시다.

## print_fahrenheit_value 함수 작성하기
마지막 함수입니다. 본 함수는 출력값이 없고 입력값의 결과를 화면에 출력해 주기만 합니다. 함수의 구성은 다음과 같습니다.

내용           | 구성
--------       | ---
함수명      | print_fahrenheit_value
input 변수(argument) | float type의 celsius_value, float type의 fahrenheit_value
Process     | 입력 받은 celsius_value와 fahrenheit_value를 화면상에 출력해줍니다. 출력시 `섭씨온도 :`, `화씨온도 :` 가 포함이 되어야 합니다.
output 값(return value)  | 없음. output 값이 없을 경우 `return 변수명` 부분을 생략하면 됩니다.

`python shell`에서 test 해보면 다음과 같이 실행됩니다.
```python
>>> import fahrenheit_converter as fc
>>> fc.print_fahrenheit_value(10.3,20.3)
섭씨온도 : 10.3
화씨온도 : 20.3
```
어떻게 보면 굉장히 간단한 함수입니다. 입력받은 값을 그대로 출력만 해주면 되기 때문입니다.  단지 `섭씨온도`와 `화씨온도`등 메세지가 정확히 출력하도록 오타 없이 입력해주기 바랍니다.

## main 함수 수정하기
이제 마지막으로 할 것은 각 함수들을 엮어서 우리가 원하는 화씨 변환기 프로그램을 완성해 주는 것입니다. 이를 위해서는 `main` 함수의 수정이 필요합니다. `main`함수에 ` # ===Modify codes below=================` 아랫 부분에 다음의 지시사항에 따라 코드를 작성해주기 바랍니다.

1. input_celsius_value 함수를 호출하고 그 결과 값을 celsius_value변수에 저장합니다.
2. celsius_value을 convert_celsius_fahrenheit 함수의 입력 값으로 하여 convert_celsius_fahrenheit 함수를 호출하고, 그 결과 값을 fahrenheit_value 변수에 저장합니다.
3. celsius_value와 fahrenheit_value을 print_fahrenheit_value 함수의 입력값으로 하여 print_fahrenheit_value 함수를 호출합니다.

굉장히 간단하지만 용어가 익숙치 않아 헷갈릴수 있습니다. 함수는 우리가 만들어 쓰는 것도 있지만 이미 파이썬에서 제공해주는 함수를 사용하는 경우도 많습니다. 예를 들면 `print` 나 `input` 같은 것들이 그런 종류의 함수입니다. 이런 함수들을 built-in 함수라고 합니다. 아래 코드를 봅시다.
```python
abc = input("What's Your Name? ")
print(abc)
```
위의 코드를 `main` 함수의 작성 설명 방식대로 한다면 다음과 같이 적을 수 있습니다.

1. "What's Your Name? "을 input 함수의 입력 값으로 하여 input 함수를 호출하고, 그 결과를 abc 변수에 저장합니다.
2. abc를 print 함수의 입력값으로 하여 print 함수를 호출합니다.

수업 시간에 설명을 잘 들었다면, 무리없이 이해했을 거라 봅니다. 문의사항이 있으면 Slack을 활용합시다.

## 결과 출력하기
실제 코드가 다 작성되어 `python fahrenheit_converter.py` 을 실행하면 아래와 같이 결과를 볼 수 있을 것입니다. 당연히 입력 부분은 수강자가 직접 입력을 해주어야 프로그램 진행됩니다.

```bash
본 프로그램은 섭씨를 화씨로로 변환해주는 프로그램입니다
============================
변환하고 싶은 섭씨  온도를 입력해 주세요 : 32.2
섭씨온도 : 32.2
화씨온도 : 89.96000000000001
===========================
프로그램이 종료 되었습니다.
```

## 숙제 template 파일 제출하기 (윈도우의 경우)
1. <kbd>windows</kbd><sup id="windows"></sup>+<kbd>r</kbd>를 누르고 cmd 입력 후 확인을 클릭합니다.
2. 작업을 수행한 폴더로 이동 합니다.
3. 밑에 명령어를 cmd창에 입력합니다.
```bash
submit.bat [YOUR_HASH_KEY]
```

## 숙제 template 파일 제출하기 (Mac or Linux)
1. 터미널을 구동합니다.
2. 작업을 수행한 디렉토리로로 이동 합니다.
3. 밑에 bash창을 입력합니다.
```bash
./submit.sh [YOUR_HASH_KEY]
```

참고로 lab assignment 제출은 진행 중간중간해도 문제가 없습니다. 제대로 작성되었다면 아래와 같은 메세지를 확인할 수 있을 것이다.

```bash
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
print_fahrenheit_value |       PASS |             Good Job
convert_celsius_fahrenheit |       PASS |             Good Job
                main |       PASS |             Good Job
 input_celsius_value |       PASS |             Good Job
-------------------- | ---------- | --------------------
```
## Next Work
lab_4를 모두 끝냈습니다. 스스로의 끈기와 열정을 칭찬하고 시원한 맥주 한잔 하면서 자축하길 바랍니다. 처음으로 여러분은 단순한 수정이 아닌 스스로의 프로그램을 만들어보았습니다. 앞으로의 모든 숙제는 이런식으로 작성이 되니 스스로 하지 않았다면 다시한번 시도해서 완벽히 이해하고 넘어가길 바랍니다.

> **Human knowledge belongs to the world** - from movie 'Password' -
