resident_number = input("주민등록번호를 입력하세요 (예: 000101-1234567): ").strip()
parts = resident_number.split("-")

gender_code = parts[1][0]  


gender = "남자" * (int(gender_code) % 2) + "여자" * ((int(gender_code) + 1) % 2)


birth_info = f"{parts[0][:2]}년생 {int(parts[0][2:4])}월 {int(parts[0][4:6])}일생"


masked_back = parts[0] + "-" + parts[1][0] + "+" * 6


print(f"성별: {gender}")
print(f"생년월일: {birth_info}")
print(f"뒷자리: {masked_back}")
