# iot-prev-study-2025
2025 iot 개발자과정 선행학습

## 1일차
기본 과정 설명 및 개발환경 설정, 파이썬 기본학습

### 과정소개

### 개발환경 설치
- 수업진행방식
    - pc카카오톡,zoom,chrome
    - 반디집 다운로드(반디집은 회사,개인 저작권 문제 없음)

- 깃허브
    - 깃 다운
    - 깃허브 로그인
    - 깃허브 데스크탑-체크박스 위에꺼/본인 이메일
    - repository만들기-add gitingnore
    - c드라이브 내 루트에 Dev, Source 폴더 만들기
    - 깃허브데스크탑-깃 repositoty와 c\source 경로를 clone

    - 깃허브 사용법법
        1. 리모트 리포지토리 생성
        2. 깃허브데스크톱으로 로컬 리포지토리로 클로닝
        3. 로컬에서 작성 후 커밋 후
        4. 리모트로 푸시
        5. 다른 사용자가 리모트에 있는 최신 내용 풀

- 글꼴
    - https://hangeul.naver.com/font 나눔글꼴다운로드
    - 나눔고딕 ttf /D2coding

- vscode다운로드 - https://update.code.visualstudio.com/1.96.3/win32-x64/stable
    - VSCodeSetup-x64-1.96.3
    - VSCODE 위치 -C:\Dev\IDE\Microsoft VS Code

    - 확장-KOREAN MICROSOFT사 설치
    - 설정 창(CTRL + ,)에 ZOOM입력 후 마우스휠 체크  =>코드창에서 컨트롤 마우스휠로 확대해서 코드 작성 
    - 설정-FONT FAMILY 검색 -EDITOR  font family -D2Coding,   추가=> 알파벳 오의 소문자, 대문자, 숫자 0 구분 /oO0

- markdown yiyi wang을 확장에서 다운로드 
    - ctrl shift v하면 디자인 화면을 미리보기로 

### 마크다운 학습

#### 마크다운이란?
- Markdown은 웹페이지에 리포팅을 하기 위한 마크업 언어
    - 주요사용처-위키피디아, 나무위키, 깃허브, 주피터노트북 등...
    - 문법이 간단하고 쉽게 배울 수 있음
    - 표준이 없는 단점

1. 번호 목록
    1. 첫번째 목록
    2. 두번째 목록
        1. 두번째 하위 목록 1
        2. 두번째 하위 목록 2
            - 일반목록


##### 기본 문법
- 링크 사용법
[네이버](https://www.naver.com)
- 이미지 사용법
![환수사 이미지 보기](https://ssl.pstatic.net/melona/libs/1522/1522020/aa5b48b7e7f7e1e6d44c_20250109174152630.jpg)

###### 추가사항
추가사항입니다.

### 파이썬 학습

#### 파이썬이란?
- 귀도 반 로썸이 1990년경에 개발한 초간단! 인터프리터 프로그래밍 언어

##### 파이썬 특징
- 컴파일러언어(exe실행파일이 생성되는 언어)가 아닌 .py파일로 바로 실행할 수 있는 인터프리터언어
- 객체지향언어
- 아주 쉬운 언어(진입장벽 낮음)
-프로그래머가 아닌 과학자들도 쉽게 프로그램개발에 진입
- https://www.tiobe.com/tiobe-index/ 에서 2020년 이후 1위 고수
- 빅데이터분석, 인공지능, 웹개발 등 다양한 분야 활용

##### 파이썬 설치
- install now로 설치하면 안됨!  custom 경로 설정버전으로 설치 
- add python.exe to PATH 체크
- C:\Dev\Lang\Python313
- disable path length limit 체크
- 설치 확인
    - cmd(윈도우 전용) 또는 powershell 실행 후 python 입력
    C:\Users\Admin>python
    Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    
    문자 >>> import sys
    문자 >>> sys.executable
    'C:\\Dev\\Lang\\Python313\\python.exe'         파이썬에서는 역슬래쉬n이 있기에 경로에서의 역슬래쉬 2개를 씀
    문자 >>> exit()

    C:\Users\Admin>python --version
    Python 3.13.1
   
-github desktop에서 ctrl +shift +a로 vscode 열기기
- vscode 확장에서 python 설치
- 확장자 .py

- 탐색기에서 day01폴더 생성
- py01_first.py 파일 생성
- ctrl + f5 , python debugger



## 첫번째 커밋하기
summary 입력
commit 버튼
push 버튼
