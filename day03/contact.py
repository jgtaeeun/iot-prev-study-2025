# 연락처를 담는 클래스

# 2. 클래스 정의
class Contact : 
    # 클래스에 속하는 함수들은 인자의 첫번째에 self를 받드시 기재!!!

    def __init__(self, name, phone, email, addr):  #객체 생성시 초기화
        self.__name = name  #클래스 멤버변수에 함수 매개변수를 할당
        self.__phone = phone
        self.__email = email
        self.__addr =  addr        
    
    # 4. 사용자가 편하게 볼 수 있게 출력을 변경
    def __str__(self):
        str_res = ('이름:' + self.__name + '\n'
                   '연락처:'+ self.__phone + '\n'
                   '이메일:'+ self.__email + '\n'
                   '주소:'+ self.__addr)
        return str_res
    
    def isNameExist(self, name):
        if self.__name == name :
            return True
        else :
            return False
        
    # 각 멤버변수 가져오기
    def getName(self):
        return self.__name
    def getPhone(self):
        return self.__phone
    def getEmail(self):
        return self.__email
    def getAddr(self):
        return self.__addr
    