#  Windows 에서 Atom Editor 설치, 실행하기
  
  Atom은 Github에서 만든 에디터로 다양한 프로그래밍 언어의 편집기로 사용할 수 있도록 고안된 도구이다. 무료이며 플로그인으로 기능을 쉽게 확장할 수 있다. 또한 HTML, CSS, JavaScript와 같은 웹기술로 화면을 구현했기 때문에 웹페이지를 편집하듯이 UI를 제어할 수 있다.
  
##  < Atom editor 설치하기 >


###  1.  Atom 공식 홈페이지 <https://atom.io/> 메인 화면에 "Download Windows Installer" 버튼을 클릭하여 설치 파일을 다운로드 받는다.   

![Atom 공식 홈페이지](./Atom_windows_img/atom_page.jpg)


###  2.  다운로드 받은 Atom 설치 파일(AtomSetup.exe) 을 실행한다.
 
![AtomSetup.exe](./Atom_windows_img/atom_setup.jpg)


####  AtomSetup.exe 파일을 실행하면 아래 이미지가 뜨면서 설치가 시작된다.

![install_atom](./Atom_windows_img/install_atom.jpg)


####  설치 완료
![finished_install](./Atom_windows_img/atom.jpg)

  
  
  
##  < Atom Editor 에서 Python 실행하기>


###  1. Python 코드 실행을 위한 패키지 설치하기
  
####  1) Atom 실행 후 File -> Settings 클릭 또는 Ctrl+Comma 를 입력한 후 Install 메뉴를 클릭한다.

![install_package](./Atom_windows_img/install_package.jpg) 


####  2) Search packages 에 아래 두 패키지를 검색하여 설치한다.
 > __autocomplete-python__
   
 > __script__


####  3) 만약 script 패키지에서 아래에서 보이는 것과 같은 에러가 난다면 다음 url을 클릭하여 Git을 설치한 다음 2)번과 같은 방법으로 다시 script 패키지를 설치한다. <https://git-scm.com/download/win>

![script_error](./Atom_windows_img/script_error.jpg) 




###  2. Python 실행하기

####  1) File > New File (Ctrl + N) 을 클릭해 파일을 하나 생성한다.


####  2) 오른쪽 하단에 Python이 아닌 다른 언어로 설정되어 있다면 Python 으로 바꿔준다.


####  3) 실행하고 싶은 Python 코드 작성 후  Ctrl + Shift + b 단축키를 클릭하여 실행시킨다.


![run_python.exe](./Atom_windows_img/run_python_code.jpg) 
