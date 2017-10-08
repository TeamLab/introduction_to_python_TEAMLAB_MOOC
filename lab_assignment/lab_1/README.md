Lab #1 - arithmetic_function 숙제 제출 연습하기
=======
Copyright 2017 © document created by teamLab.gachon@gmail.com

## Introduction
K-MOOC Python과 Gachon CS50에서는 모든 숙제를 TeamLab에서 개발된 자동 채점 시스템(Gachon Autograder)를 통해 제출하게 됩니다.  본 실습에서는 자동 채점 시스템을 사용하여 숙제를 제출하는 과정을 연습합니다.  아직 파이썬의 주요 내용을 배우지 않은 상태이기 때문에 매우 간단한 사칙연산 코드를 작성합니다.

## Lab Assignment 진행을 위한 lab_1.zip 다운로드
첫 번째 할일을 숙제 제출과 숙제 진행을 위해 숙제파일이 압축된 파일인 "lab_1.zip"을 다운로드하는 것 입니다. Chrome 또는 익스플로러와 같은 웹 브라우저 주소창에 아래 주소를 입력합니다.

https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/tree/master/lab_assignment/lab_1 

다운로드를 위해 `View Raw` 또는 `Download` 버튼을 클릭합니다. 또는 아래 다운로드 링크를 클릭하면 자동으로 다운로드가 됩니다. [Lab 1 - 다운로드](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/raw/master/lab_assignment/lab_1/lab_1.zip)

일반적으로 다운로드 된 파일은 사용자 폴더내 "다운로드" 폴더로 이동하게 됩니다. 

<kbd>windows</kbd><sup id="windows"></sup>+<kbd>e</kbd>를 누르면 일반적으로 왼쪽 상단에 나타나는 "다운로드" 폴더에 다운로드 된 `lab_1.zip` 파일을 작업 폴더로 이동한 후 압축해제 후 작업하길 바랍니다.

## arithmetic_function.py 내용 보기
다음으로 압축해제 된 `arithmetic_function.py` 파일의 구조를 파악해 봅니다. 구조 파악을 위해서는 atom으로 해당 파일을 열어야 하는데 아래의 과정을 거쳐 atom으로 파일을 오픈합니다.

1. <kbd>windows</kbd><sup id="windows"></sup>+<kbd>r</kbd> 을 누른 후, `cmd`를 입력하여 검은색 화면인 콘솔창을 오픈합니다.
2. `cd workspace`등을 이용해서 여러분의 작업폴더로 이동합니다.
3. 작업폴더에는 이미 숙제 압축 파일이 해제되어 있어야 합니다.
4. `atom .` 명령을 사용하여 atom을 실행시키고, 왼쪽 상단 메뉴트리에서 `arithmetic_function.py` 클릭하여 파일을 오픈합니다.
5. 어려울 경우, 소개 영상을 다시 봅니다.

모든 숙제 template 파일은 동일하게 아래 세 가지 함수로 나뉘게 됩니다.

분류           | 의미 
--------       | ---
test 함수      | 숙제를 실제 수행해야 할 함수로, 함수내에 `Modify codes below` 라는 문구가 작성되어 있습니다,  사용자는 해당 문구내 부분을 수정하여야 합니다.
helper 함수    | 숙제 진행을 원활히 돕기 위해 출제자가 작성한 함수, 따로 수정이 필요없는 함수로 수정할 경우, 숙제 제출이 불가능할 수도 있습니다.
main 함수       | template 제일 하단에 있는 숙제 test용 코드로 `def main():` 안에 작성됨, 해당 코드는 실제 코드가 바르게 작성되었을 경우, 실행 결과에 대해서 상세히 기술되어 있습니다.

`arithmetic_function.py` 의 경우 아래 4가지의 test 함수와 하나의 main 함수로 구성되어 있습니다.

- addition(a, b) - a,b 두 개의 숫자가 입력될 경우 두 수의 합을 반환합니다. 
- minus(a, b) - a,b 두 개의 숫자가 입력될 경우 a에서 b를 뺀 값을 반환합니다.
- multiplication(a, b) - a,b 두 개의 숫자가 입력될 경우 두 수의 곱을 반환합니다.
- division(a, b) - a,b 두 개의 숫자가 입력될 경우 b로 a를 나눈 값을 반환합니다.

addition 함수의 경우, 아래와 같이 작성되어 있습니다.
```python
def addition(a, b):
    # '''
    # Input:
    #   -a: 실수 값 (Integer of float)
    #   -b: 실수 값 (Integer of float)
    # Output:
    #   -두 값의 합
    # Examples:
    #   >>> addition(3,5)
    #   8
    #   >>> addition(3,2)
    #   5
    # '''
    # pass
    # ===Modify codes below=============

    result = None 

    # ==================================

    return result
```   

위 함수에서 `# ===Modify codes below=============` 윗 부분까지가 함수에 대한 간략한 설명입니다. 

`# Input:` 부분은 이 함수에 입력되는 값의 유형에 대해 설명하고, `# Output:` 부분은 이 함수의 결과값에 대해 서술합니다. 중요한 부분은 `# Examples:` 입니다. 

해당 부분 하단에는 이 함수를 실제 수행하였을 때 나올 수 있는 결과 값에 대해서 작성되어 있습니다. 이를 실제 확인하게 위해서는 파이썬 쉘을 실행 시켜야 합니다. 

파이썬 쉘은 `python` 라고 치면 나오는 프로그래밍 환경을 의미합니다. 파이썬 쉘을 실행후 아래와 `>>>` 이후에 있는 코드를 입력해 봅니다. 

```bash
C:<작업경로\lab_1> python
Type "help", "copyright", "credits" or "license" for more information.
>>> import arithmetic_function as af
>>> result = af.addition(10,5)
>>> print (result)
None
```

첫 번째 `import` 문은 작성된 프로그램을 호출하는 명령어입니다. 우리가 현재 작성한 프로그램 파일이름은 "arithmetic_function.py"로 여기서 확장자인 .py를 제외하고 입력합니다.
 
뒤에 붙은 `as af` 의미는 `arithmetic_function`을 `af`라는 이름으로 부르겠다는 의미입니다. 두 번째 코드는 `arithmetic_function` 코드에 있는 `addition` 이라는 함수를 부른다는 의미입니다. 

해당 함수는 입력 값으로 a와 b를 받아야 되는데 여기서는 a와 b과 각각 10과 5로 매칭됩니다. `result = af.addition(10,5)`함수의 결과값이 `result`라는 이름의 변수로 저장된 다는 의미입니다. 

마지막 코드는 `result`의 결과를 출력하라는 뜻입니다. 현재까지 코드를 수정된 것이 없기 때문에 현재 결과 값은 `None`으로 설정되어 있습니다.  

## arithmetic_function.py 수정 하기
실제 수강자가 고쳐야할 부분은 아래 코드 부분입니다. 본 함수의 목적이 입력된 두 값의 덧셈이므로 `result = None`을 `result = a+b`로 수정해 주면 된다. 나머지 함수들도 각 함수의 목적에 맞게 `result = None`을 부분을 수정합니다.

```python
   # ===Modify codes below=============

    result = None 

    # ==================================
```
##### 제대로 수정되었는지를 확인하기 위해서는 수정된 프로그램을 실행시켜 봅니다.  
1. <kbd>windows</kbd><sup id="windows"></sup>+<kbd>r</kbd>를 누르고 cmd 입력 후 확인을 클릭합니다.
2. 아까 작업폴더로 이동한 경로로 이동을 합니다.
3. `python arithmetic_function.py` 입력합니다

이때 실행되는 코드는 `main()` 함수안에 있는 아래 코드입니다. 

`print` 문은 괄호 안에 있는 값을 화면에 출력하는 명령어로 아래 코드는 먼저 `Addition Test` 라는 문장을 출력하고 다음으로 `addition(3,5)`의 결과를 출력합니다. 

각각의 출력되는 기대 값은 `#` 기호옆 주석<sup id="comment"></sup>으로 작성되어 있습니다. 

숙제 진행시 수강자가 수정한 프로그램을 실행하면서 나오는 결과값들이 `main()` 함수 내의 주석 처리된 기댓값들과 같은지 확인하면 됩니다. 

`main()` 함수는 숙제 제출에 영향을 주지 않는 함수로 사용자가 원할 경우 자유로운 수정이 가능합니다.

```python
def main():
    print ("Addition Test")
    print (addition(3,5)) # Expected Result: 8
    print (addition(10,5) == 15) # Expected Result: True
    print ("Addition Test Closed \n")


    print ("Minus Test")
    print (minus(3,5)) # Expected Result: -2
    print (minus(10,5) == 5) # Expected Result: True
    print (minus(10,15) == 5) # Expected Result: False
    print ("Addition Test Closed \n")

    print ("Multiplication Test")
    print (multiplication(3,5)) # Expected Result: 15
    print (multiplication(10,5) == 50) # Expected Result: True
    print (multiplication(10,-3) == 20) # Expected Result: False
    print ("Addition Test Closed \n")

    print ("division Test")
    print (division(5,5)) # Expected Result: 1
    print (division(5,4)) # Expected Result: 1.25
    print (division(10,5) == 2) # Expected Result: True
    print (division(10,-3) == 0.33333) # Expected Result: False
    print ("division Test Closed \n")
```

## 숙제 template 파일 제출하기
1. <kbd>windows</kbd><sup id="windows"></sup>+<kbd>r</kbd>를 누르고 cmd 입력 후 확인을 클릭합니다.
2. 아까 작업폴더로 이동한 경로로 이동을 합니다.
3. 밑에 bash창을 입력합니다.
```bash
python submit.py
```

위 명령어를 입력 하면, 아래와 같은 내용이 띄면서 Login ID와 Password를 물어보게 될 것입니다. http://theteamlab.io 웹 페이지에 가입시 사용했던 Login ID와 비밀번호를 입력합니다.

```bash
== Submmting solutions | arithmetic_function.py
Login ID:
Password :
```

본 명령을 실행하여 프로그램의 문법상 에러가 없을 경우, 아래와 같은 형태로 숙제 제출 확인 메세지를 받게됩니다.

```bash
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
            division |       PASS |             Good Job
               minus |       PASS |             Good Job
      multiplication |       PASS |             Good Job
            addition |       PASS |             Good Job
-------------------- | ---------- | --------------------
```




## Next Work
첫 번째 Lab Assignment를 무사히 마친 것을 축하합니다. 아마 지금쯤이면 상당히 진이 빠져 있는 상태일 것이다. 아직 우리에게는 재미있는 Lab Assignment가 많습니다. 할 수 있습니다.

> **Human knowledge belongs to the world** - from movie 'Password' -

