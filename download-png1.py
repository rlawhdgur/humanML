import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savenmae = 'test.png'

# 다운로드
urllib.request.urlretrieve(url, savenmae)
print("저장되었습니다.")