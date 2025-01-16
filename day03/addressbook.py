# 주소록 프로그램

import contact 
import os           #운영체제에 사용할 기능


# 콘솔화면 클리어 함수
def clear_console():
    command = 'clear'               #리눅스, 유닉스 클리어 명령어
    if os.name in ('nt', 'dos'):    #운영체제가 윈도우라면
        command = 'cls'             #윈도우 클리어 명령어
    os.system(command)              #콘솔에 명령어 실행

# 파일 DB 저장 함수
def save_contact(lst_contact):
    f = open('./day03/address_db.txt', mode='w', encoding='utf-8')
    for i in lst_contact:
        f.write(i.getName() + '/') 
        f.write(i.getPhone() + '/') 
        f.write(i.getEmail() + '/') 
        f.write(i.getAddr() + '\n') 
    
    f.close()                   #파일을 열었으면, 끝난 후 파일을 반드시 닫아줘야함!!
# 파일 DB 로드 함수
def load_contact(lst_contact):
    f = open('./day03/address_db.txt', mode='r', encoding='utf-8')
    while True:
        line =  f.readline()
        if not line :
            break
       
        # \n으로 indexarray 오류발생. \n을 리스트 저장전에 삭제해야함
        lines = line.replace('\n','').split('/')     #lines는 4개의 문자열을 가지는 리스트
        address = contact.Contact(name = lines[0], phone= lines[1], email= lines[2], addr= lines[3])
        lst_contact.append(address)
    f.close()

# 연락처를 입력받는 함수
def set_address():
    try : 
        name , phone, email, addr = input('정보입력(이름, 연락처, 이메일, 주소 순): ').split(',')
        # print(name, phone, email, addr)
        # 객체 Contact 생성, 리턴
        address= contact.Contact(name, phone, email, addr)
        return address
    except ValueError :
        print('데이터를 정확히 입력하세요')
        return None     
    
   
#연락처 출력 함수
def get_address(lst_contact):
    for i in lst_contact:
        print(i)

#연락처 삭제 함수
def del_address(lst_contact, name):
    result=False
    for i, item in enumerate(lst_contact):  #각 객체에 번호를 매겨주는 클래스
        if item.isNameExist(name) :
            del lst_contact[i]               #메모리에서 완전 삭제    
            result   = True          
 
    return  result 
        

# 프로그램 실행 함수
def run():
    # 주소정보들을 담을 변수


    lst_contact=[]
    load_contact(lst_contact)
    clear_console()


    while True :
        sel_menu = get_menu()
        if sel_menu == 1 :
            if set_address() is  None :
                pass
           
            else :
                lst_contact.append(set_address())
                print('추가되었습니다.')
            input()

        elif sel_menu == 2 :
            get_address(lst_contact)
            input()

        elif sel_menu == 3 :
            name = input('삭제할 이름을 입력하시오: ')
            if del_address(lst_contact, name):
                print('삭제되었습니다.')
                input()     #단순입력대기
            else :
                print('존재하지 않는 이름입니다.')
                input()

        elif sel_menu == 4:
            save_contact(lst_contact)
            break
        else :
            pass
           
        clear_console()
# 메뉴 구성
def get_menu():
    str_menu=('주소록 프로그램 v1.0\n' 
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n'
            )
    print(str_menu)
    
    # 예외처리 try-except
    try  :
        menu_num =  int(input('메뉴입력: '))  #숫자를 표현하는 문자
    except Exception: 
       menu_num = 0  #메뉴와 관계없는 숫자  

    return menu_num
    

if __name__ == '__main__':
    # pass      #if , for, while, 함수 등에서 오류를 없애는 방법
    run()
    
