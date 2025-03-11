import sys

display = '''
----------------------------------------------------------
1.명함입력, 2.명함수정, 3.명함삭제, 4.명함목록보기, 5.종료
----------------------------------------------------------
메뉴를 선택하세요 >>> '''

names = []
phones = []
companies = []

while True:
    menu = input(display).strip()
    
    if menu == '1':
        print("명함입력")
        name_tmp = input("이름: ").strip()

        names.append(name_tmp)
        phones.append(input("전화번호: ").strip())
        companies.append(input("소속: ").strip())

        print(f"{name_tmp}님의 명함이 추가되었습니다.")

    elif menu == "2":
        print("명함수정")

    elif menu == "3":
        print("명함삭제")

    elif menu == "4":
        print("명함목록보기")

    elif menu == '5':
        print("프로그램 종료")
        sys.exit()
    else:
        print("메뉴선택을 잘못하셨습니다.")