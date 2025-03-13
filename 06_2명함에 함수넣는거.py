display = """
-------------------------------------------------------------------
1. 명함 입력, 2. 명함 수정, 3. 명함 삭제, 4. 명함 목록 보기, 5. 종료
-------------------------------------------------------------------
메뉴를 선택하세요 >>> """


# 명함 정보를 저장할 리스트
names = []
phones = []
companies = []


def menu1():
    print("명함입력")
    name_tmp = input("이름: ").strip()

    names.append(name_tmp)
    phones.append(input("전화번호: ").strip())
    companies.append(input("소속: ").strip())

    print(f"{name_tmp}님의 명함이 추가되었습니다.")


def menu2():
    print("명함 수정")
    search_name = input("수정할 명함의 이름을 입력하세요: ").strip()

    if search_name in names:
        index = names.index(search_name)  # 해당 이름의 인덱스를 찾음
        print(
            f"🔹 현재 정보: 이름: {names[index]}, 전화번호: {phones[index]}, 소속: {companies[index]}"
        )

        # 새 정보 입력
        phones[index] = input("새로운 전화번호: ").strip()
        companies[index] = input("새로운 소속: ").strip()

        print(f"✅ {search_name}님의 명함이 수정되었습니다.")
    else:
        print("⚠ 해당 이름의 명함이 없습니다.")


def menu3():
    print("명함 삭제")
    search_name = input("삭제할 명함의 이름을 입력하세요: ").strip()

    if search_name in names:
        index = names.index(search_name)  # 해당 이름의 인덱스를 찾음

        # 리스트에서 해당 인덱스의 요소 삭제
        names.pop(index)
        phones.pop(index)
        companies.pop(index)

        print(f"🗑 {search_name}님의 명함이 삭제되었습니다.")
    else:
        print("⚠ 해당 이름의 명함이 없습니다.")


def menu4():
    print("\n📜 [명함 목록]")

    if len(names) == 0:
        print("📭 저장된 명함이 없습니다.")
    else:
        for i in range(len(names)):
            print(
                f"{i+1}. 이름: {names[i]} | 전화번호: {phones[i]} | 소속: {companies[i]}"
            )


while True:
    menu = input(display).strip()

    # 1. 명함 입력
    if menu == "1":
        menu1()

    # 2. 명함 수정
    elif menu == "2":
        menu2()

    # 3. 명함 삭제
    elif menu == "3":
        menu3()

    # 4. 명함 목록 보기
    elif menu == "4":
        menu4()

    # 5. 종료
    elif menu == "5":
        print("🚪 프로그램을 종료합니다.")
        break

    # 잘못된 입력 처리
    else:
        print("⚠ 올바른 번호를 입력하세요.")
