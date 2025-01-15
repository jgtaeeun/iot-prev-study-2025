print('함수')    #내장함수

#사용자 정의 함수
def add(a, b) :
    result = a + b
    return result

def diff(a, b):
    result = a - b
    return result
    
def multiple( a, b ):
    result = a * b
    print(result)
   # return              #아무것도 반환할 게 없으면 return 생략

def divide():
    result = 100 / 4 
    print('나누기 결과' , result)


x = 11
y = 22
z = add (x, y)
print('합의 결과는' , z)

x = 101
y = 203
print ('합의 결과는' , add(x, y))


x = 35
y = 15
print('차의 결과는', diff(x, y)) 

x = 30
y = 10
z = multiple(x, y)    #300     
multiple(x, y)        #300
print(z)              #None

divide()

'''내장함수'''
print(max(1,3,7,15))
print(min(1,3,7,15))
print(abs(-5))
print(pow(2,10))
print(2 ** 10)