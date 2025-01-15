# 흐름제어
# if, for, while

## int, float, double(복소수화)

# age = input('나이를 입력하세요 > ')   # age변수에 문자열이 입력된다
age = int (input('나이를 입력하세요 > '))
# print("만나이",age-2)
age = age -2

## if문을 시작하겠다는 의미하는 마지막 단어 :
if age <19 :
    print('미성년자입니다.')
elif age >= 65:
    print('성인-고령층입니다.')
else:
    print('성인-청년,중년층 입니다.') 




