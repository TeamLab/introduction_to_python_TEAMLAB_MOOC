Lab #11 - File IO Example (file_io_example)
=======
Copyright 2017 © document created by TeamLab.Gachon@gmail.com

## Introduction

[PDF 파일 다운로드](https://github.com/TeamLab/introduction_to_python_TEAMLAB_MOOC/raw/master/lab_assignment/lab_9/lab_9.pdf)

이번 Lab은 쉽습니다. 다행이도요. 쉽습니다. 즐겁우시죠. 이번 Lab은 Text Handling 시리즈의 첫 번째 Lab 입니다. 이번 Lab의 목표는 간단한 파일을 다운로드 받고, 파일안에 있는 정보를 추출하는 것 입니다. 함수도 5개 밖에 없습니다. 바로 본론으로 들어가겠습니다.

## 숙제 파일(lab_9.zip) 다운로드
 먼저 해야 할 일은 숙제 파일을 다운로드 받는 것 입니다. Chrome 또는 익스플로러와 같은 웹 브라우저 주소창에 아래 주소를 입력합니다.

 [https://github.com/TeamLab/introduction_to_python_TEAMLAB_MOOC/blob/master/lab_assignment/lab_9/lab_9.zip](https://github.com/TeamLab/introduction_to_python_TEAMLAB_MOOC/blob/master/lab_assignment/lab_9/lab_9.zip)

 다운로드를 위해 `View Raw` 또는 `Download` 버튼을 클릭합니다. 또는 아래 다운로드 링크를 클릭하면 자동으로 다운로드가 됩니다. [Lab file_io - 다운로드](https://github.com/TeamLab/introduction_to_python_TEAMLAB_MOOC/raw/master/lab_assignment/lab_9/lab_9.zip)
 다운로드 된 `lab_9.zip` 파일을 작업 폴더로 이동한 후 압축해제 후 작업하시길 바랍니다.
 압축해제 하면 폴더가 `linux_mac`과 `windows`로 나눠져 있습니다. 자신의 OS에 맞는 폴더로 이동해서 코드를 수정해 주시기 바랍니다.

 다운로드 폴더로 이동하면 `file_io_example.py` 파일이 다운로드 되어 있습니다.

 본 랩에서 사용할 예제파일은 `1984.txt`입니다. 이미 여러분의 각 폴더에 들어가 있을 것입니다. 절대 파일을 수정하지 마시기 바랍니다.


## file_io_example.py 파일 Overview
`atom`로 `file_io_example.py`을 열어 전체적인 개요를 확인합니다. 이번 Lab은 오직 5개의 함수로만 구성되어 있으며, Main 함수는 존재하지 않습니다.

이제 수정해야 할 함수 리스트를 보겠습니다.

함수           | 설명
--------       | ---
get_file_contents | 문자열값으로 filename을 입력받아 해당 파일에 존재하는 모든 text 데이터를 문자열 형태로 반환함
get_number_of_characters_with_blank | 문자열값으로 filename을 입력받아 해당 파일에 존재하는 모든 글자의 갯수를 integer 값으로 반환함
get_number_of_characters_without_blank | 문자열값으로 filename을 입력받아 해당 파일에 존재하는 모든 글자의 갯수를 공백을 제외하고 integer 값으로 반환함. 단 여기서 공백은 " ", "\t", "\n" 을 의미함
get_number_of_lines | 문자열값으로 filename을 입력받아 해당 파일에 존재하는 모든 줄(line)수를  integer 값으로 반환함. 이때 마지막 줄은 count에서 제외함
get_number_of_target_words | 문자열값으로 filename과 찾고자하는 target_words을 입력받아 해당 파일에 존재하는 target_words와 같은 글자의 수를 대소문자와 상관없이 integer 값으로 반환함


## 결과확인
너무 쉽게 하셨을 겁니다. python shell에서 test 한다면 다음과 같은 결과가  나올 것이다.

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

###숙제 template 파일 제출하기 (윈도우의 경우)
1. <kbd>windows</kbd><sup id="windows"></sup>+<kbd>r</kbd>를 누르고 cmd 입력 후 확인을 클릭합니다.
2. 작업을 수행한 폴더로 이동 합니다.
3. 밑에 명령어를 cmd창에 입력합니다.
```bash
install.bat
submit.bat [YOUR_HASH_KEY]
```

### 숙제 template 파일 제출하기 (Mac or Linux)
1. 터미널을 구동합니다.
2. 작업을 수행한 디렉토리로로 이동 합니다.
3. 밑에 bash창을 입력합니다.
```bash
bash install.sh
bash submit.sh [YOUR_HASH_KEY]
```
> backend.ai 서비스의 업데이트에 의해 실행전 반드시 `bash install.sh` 또는 `install.bat` 수행을 바랍니다.

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
이번 랩은 너무 쉬우서 아마도 잠시만에 끝내신 분들이 많으실거 같습니다. 걱정하지 않으셔도 됩니다 아직도 우리에겐 csv의 Lab이 남아있습니다.

> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes
