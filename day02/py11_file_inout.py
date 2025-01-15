# 파일 입출력

# a(추가) , r ,w

#쓰기
#f = open('textfile.txt' , mode = 'w' )

# f = open('./day02/textfile.txt' , mode = 'w' , encoding='utf-8')
# f.write('저는 한국사람입니다.')
# f.close()

#추가
# f = open('./day02/textfile.txt' , mode = 'a' , encoding='utf-8')
# f.write('저는 한국사람입니다.\n')
# f.write('남자입니다.\n')
# f.close()
# print('파일이 생성되었습니다.')

#읽기
f = open('./day02/textfile.txt' , mode = 'w' , encoding='utf-8')
f.write('저는 한국사람입니다.\n')
f.write('남자입니다.\n')
f.close()

f = open('./day02/textfile.txt' , mode = 'r' , encoding='utf-8')

while True :
    line = f.readline()     #한줄씩 읽기
    if not line :
        break
    print(line)

f.close