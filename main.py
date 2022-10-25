
list = []

in_token = input("연산기호 입력 : ")

a=input("첫번째 입력: ")
b=input("두번째 입력: ")
list.append(a)
list.append(in_token)
list.append(b)
for i in list:
    print(i,end= ' ')

