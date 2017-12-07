import urllib.request # urllib 모듈 호출
import re

url = "http://www.google.com/googlebooks/uspto-patents-grants-text.html" #url 값 입력
html = urllib.request.urlopen(url)	 # url 열기
html_contents = str(html.read().decode("utf8"))  # html 파일 읽고, 문자열로 변환

url_list = re.findall(r"(http)(.+)(zip)", html_contents)
for url in url_list:
    print("".join(url))  # 출력된 Tuple 형태 데이터 str으로 join
