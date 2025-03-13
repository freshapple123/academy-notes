def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def indata():
    a = int(input("숫자를 입력하세요 :"))
    return a


result = add(1, 3)
print(result)

data1 = indata()
data2 = indata()
sub(data1, data2)
