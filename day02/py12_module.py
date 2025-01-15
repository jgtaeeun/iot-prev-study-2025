# 모듈

import py10_function as calc

calc.multiple(4,5)

# math모듈 연산결과는 실수형이다.
import math
result = math.pow(2,10)          #math.pow는 실수형, 2 ** 3 은 정수형 , pow(2,3)은 정수형
print(result)

print(pow(2,10))
print(2 ** 10)

result = math.log2(4)
print(result)

## 패키지 - 모듈들을 모아둔 디렉토리(폴더)
## pip install requests 
## C:\Dev\Lang\Python313\Lib\site-packages\requests
import requests

###웹
res = requests.get('https://www.naver.com')     #네이버 사이트를 접속하라
print(res.status_code)                          #200
print(res.content)                               