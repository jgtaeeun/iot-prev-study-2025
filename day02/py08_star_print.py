# 별 찍기

'''
 *
 **
 ***
'''


# 문자열에 사용할 수 있는 연산자 +, *

# 계단모양 (왼쪽 정렬)
# for i in range(5):
#     print('*' * (i+1))

# # 계단모양 (오른쪽 정렬)
# a = 5
# for i in range(5):
#     print(' ' * ((a - 1) - i), end=' ')
#     print('*' * (i + 1))



'''
 ***
 **
 *
'''
# 계단모양 거꾸로 (왼쪽 정렬)

# num=10
# for i in range(1,num):
#     print((num - 1 - i)* '*')


# # 계단모양 거꾸로 (오른쪽 정렬)
# num=10
# for i in range(1,num):
#     print((' ') * ( i - 1 ) , end='')
#     print( (num - 1 - i ) * '*')

# # 세모모양



'''
   *
  ***
 *****
'''


num = 10
j = 1
for i in range(1,num,2):
   
    mid = (1 + num - 1 ) // 2
    update_mid = mid - j
    print(' ' * update_mid  , end='')
    print( '*'  *  i )
    j = j + 1 



