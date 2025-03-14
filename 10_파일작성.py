'''
# JSON 공부
import json

data = {"name": "홍길동", "age": 22}
with open("myinfo.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open("myinfo.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("JSON 결과:")
print(type(data))  # <class 'dict'>
print(data)        # {'name': '홍길동', 'age': 22}
'''

# Pickle 공부
import pickle

data = {"name": "홍길동", "age": 22}


with open("myinfo.pkl", "wb") as f:  # 'b' 모드 주의
    pickle.dump(data, f)

with open("myinfo.pkl", "rb") as f:  # 'b' 모드 주의
    data = pickle.load(f)

print("\nPickle 결과:")
print(type(data))  # <class 'dict'>
print(data)        # {'name': '홍길동', 'age': 22}
