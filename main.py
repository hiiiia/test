list = []

in_token = input("연산기호 입력 : ")

a=input("첫번째 입력: ")
b=input("두번째 입력: ")
list.append(a)
list.append(in_token)
list.append(b)

def calc(list):
    a= list.pop()
    b = list.pop()
    c = list.pop()
    ans = 0
    if b == '*':
        ans = int(c)*int(a)
    elif b =='+':
        ans = int(c) + int(a)
    elif b =='-':
        ans = int(c) - int(a)
    elif b =='/':
        ans = int(c) / int(a)

    return ans , a ,b,c
ans,a,b,c = calc(list)
print(f"계산기 : {c} {b} {a} = {ans}")



