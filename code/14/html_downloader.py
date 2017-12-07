import urllib.request	#urllib 모듈 호출

url = "http://storage.googleapis.com/patents/grant_full_text/2014/ipg140107.zip"
# 다운로드 URL 주소
print ("Start Download")
fname, header = urllib.request.urlretrieve(url, 'ipg140107.zip')
#urlretrieve 함수 호출 (url 주소, 다운로드 될 파일명), 결과값으로 다운로드된 파일명과 Header 정보를 언패킹
print ("End Download")

