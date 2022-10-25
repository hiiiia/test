import math

class read_poly:
    def __init__(self,flag=1):
        if(flag == 1):
            self.items=[]
            num = int(input("다항식의 최고 차수를 입력하세요 : "))
            for i in range(num, -1, -1):
                print("x^%d의 계수 : " % i, end="")
                self.items.append(int(input()))
        else:
            self.items=[]

    def degree(self):
        print(self.items)
    def add(self,polys):
        if(len(self.items) >= len(polys.items)):
            tmp_list = read_poly(0)
            tmp_list.items = self.items
            num = len(self.items)- len(polys.items)
            for i in range(num,len(self.items)):
                tmp_list.items[i] += polys.items[i-num]
            return tmp_list
        else:
            tmp_list = read_poly(0)
            tmp_list.items = polys.items
            num = len(polys.items)- len(self.items)
            for i in range(num, len(polys.items)):
                tmp_list.items[i] += self.items[i - num]
            return tmp_list

    def evaluate(self,sq):
        num = len(self.items)-1
        result = 0
        for i in range(num,-1,-1):
            result += float(self.items[num-i])*math.pow(sq,i)
        return result

    def display(self):
        num = len(self.items)-1
        for i in range(num,-1,-1):
            print(f"x^{i}의 계수 : {self.items[num-i]}")

    def inverse(self):
        num = len(self.items)
        for i in range(num):
            self.items[i] *= -1




a = read_poly()
b= read_poly()
c = a.add(b)
a.degree()
a.inverse()
a.degree()
print(a.evaluate(2))


