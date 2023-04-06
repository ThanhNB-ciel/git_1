import pandas as pd
import numpy as np
l = [1,2,3,4,5,6,7,8,9]
# print(l[8]) 

# x = int(input('nhập x = '))
# y = int(input('nhập só y'))
# if x > 8:
#     print('nay được mua ô tô')
# elif x <=8 and x >= 6:
#     print('me k đánh')
# else:
#     print(' mẹ thưởng cho ô tô')


# while (x <= 10):
#     print(x,'thanh')
#     x = x + 1
# while (x <=10):
#  if x % 2 == 0:
#         print(x, end =' ')
#     x = x + 1 
A = [];
# print(type(A))
# A.append(10)
# # print(A)
A.append(30)
A.append(100)
# print(A)
# while(x <= 15):
#     if x % 2 == 0 :
#         A.append(x)
#     x = x + 1
# print(A)
t = (1,2,3,4,5)
# print(type(t))
# for i in t :
#     print(i, end =' ')
# t1 = ( 1,3,5,7,9)
d = {'Tuan' : 26, 'Huy' : 30 ,'An' : 26}
# print(type(d))
# for key in d:
#     print(d[key])

# ss = 'Nguyen Bao Thanh'
# for s in ss : 
#     if (s !=' '):
#         print(s," ten Thanh ", end =' ')

s = 'Nguyễn Bảo Thanh AI'
# print(s.split('n'))
# import random
# a = random.randint(1,100)
# b = random.randint(1,100)
# c = random.randint(1,100)
# # print(a,b,c)
# li =[]
# for item in range(10):
#     li.append(item ** 2)
# # print(li)

# l = [item ** 2 for item in range(10)]
# # print(l)
    
# leven = []
# for item in l :
#     if item % 2 == 0:
#         leven.append(item + 3)
# # print(leven)


# s = {1,2,3,4,5}
# # print(len(s))

# d = {'name':'Nguyễn Bảo Thanh','age' : "26", 'web': 'thanhnb.com'}
# d['age'] = 28
# # print(d)

# def gb():
#     # print('Say goodbye')
#     return('iii')
# # print(gb())

# # i = int(input('nhap i vô đây'))
# def love():
#     i = int(input('nhap i vô đây'))
#     while ( i<10 ) :
#         print('thanhnb')
#         i = i +1
# # print(love())

# def tong (x,y,z):
#     t = x+y+z
#     return t
# ketqua = tong(1,2,3)
# print('Tổng là :', ketqua)


# def tong (*data):
#     t = 0
#     for item in data:
#         t = t + item 
#     return t
# ketqua = tong(10,20,30)
# print("kết quả là : ", ketqua)

def tong(*data) : 
    kq = []
    for i in data:
        tong = 0 
        for n in i: 
            tong = tong + n
        kq.append(tong)
    return kq
    
result = tong([1,2,3,4], [4,5,6,7,6])
# print('tổng là :',result)

def gia(**data) : 
    count = 0
    for name, price in data.items():
        row = "{:20}{:10}".format(name, price)
        # print(row)
        count = count + price
    return count
gia(ip = 50000, nokia = 1000, ss = 5500)
# print("{:20}{:10}".format("Tong :",gia))

def tong (n1,n2, n3, *data, **list) :
    t1 = t2 = t3 = 0
    t1 = n1 + n2 + n3
    for i in data:
        t2 = t2 + i
    for k,v in list.items():
        t3 = t3 + v 
    t = [t1,t2,t3]
    return t
data = tong(1,2,3,4,5, ip = 100, ss = 100)
# print("tong la : ",data)




def myRange( s, l, step):
    i = s
    while(i < l):
        return i 
        i = i + 1
ketqua = myRange(1,102,3)
# print("ket qua la : ", ketqua)

def countchar(*data):
    dic = {}
    for item in data:
        for i in item :
            i = i.upper()
            dic[i] = 1
            if i in dic :
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
    return dic

t = countchar( "Thanh","Baor"," Nguyeenx")
# print(t)

def myrange (*thamso): 
    start = lenght = step = 0
    if (len(thamso) == 3 ):
        strart = thamso[0]
        lenght = thamso[1]
        step = thamso[2]
    elif (len(thamso) == 2):
        start = thamso[0]
        lenght = thamso[1]
        step = 1
    else :
        start = 0
        lenght = thamso[0]
        step = 1
    i = start
    while(i < lenght) :
        yield i 
        i = i + step
B = myrange(4,100,4)
# print(list(B))
        
def tbc(*data):
    return sum(data)/len(data)
ketqua = tbc(1,2,1,2,1,3,12)
# print('tbc là :', ketqua)

def giai_thua(n) :
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a 
ketqua = giai_thua(5)
# print('tets :',ketqua)

def snt(n):
    if n < 2 : 
        return False
    for i in  range(2,int(n/2)+1):
        if n % i == 0:
            return False
    return True 
# print(snt(15))

# for i in  range(2,int(15/2)+1):
#     # print(i)

def tim_kiem(*data, x):
    for i in data :
        if data[i] == x:
            return i
        return -1 
z = (1,2,3,4,5,6)
# print(tim_kiem(z,2))


# def tim_kiem(lst, x):
#     for i in range(len(lst)):
#         if lst[i] == x:
#             return i
#     return -1
# z = (1,2,3,4,5,6)
# print(tim_kiem(z,6))
def ss(*data):
    return sorted(data)
z = ss(1,5,3,1,4,6)
# print(z)

def tong(*data):
    tong_so = 0
    for x in data :
        if x % 2 == 0 :
            tong_so += x 
    return tong_so
z = tong(1,5,3,1,4,6) 
# print('tong so là :', z)

#in số chắn 1000 đến 2000
# for i in range(1000,2001):
#     if i % 2 == 0:
def giaithua(n): 
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a 

ketqua = giaithua(5)
# print(ketqua)

# n = int(input('nhpa so n'))
# d = dict()
# for i in range(1, n + 1):
#     d[i] = i*i
# # print(d)


# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
        
#     def getString(self):
#        self.s = input("Nhập chuỗi:")
        
#     def printString(self):
#         print(self.s.upper())
# thanhnb = InputOutString()
# thanhnb.getString()
# thanhnb.printString()



# class InputOutString(object):
#    def __init__(self):
#        self.s = ""

#    def getString(self):
#        self.s = input("Nhập chuỗi:")
# # Code by Quantrimang.com
#    def printString(self):
#        print (self.s.upper())

# strObj = InputOutString()
# strObj.getString()
# strObj.printString()


import math

# c = 50 
# h = 30 
# value = []
# items = [x for x in input('Nhap gia tri của x : ').split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# # print(','.join(value))

# lines = []
# while True : 
#     x = input()
#     if s : 
#         lines.append(s.upper())
#     else:
#         break:
# for sentence in lines:
#     # print(sentence)


# line = input('nhap chuoi vo day : ')
# words = line.split() 
# words.reverse()
# # sentence = " ".join(words)
# print(words) 

def snt(n):
    if n < 2:
        return False
    else:
        for i in range(2, n +1):
            if n % i ==0:
                return False
            else:
                return True
# print(snt(11))

def total(n):
    total = 0 
    if n > 0:
        total = total + n % 10
        n = int(n/10)
    return total

z = np.array([1.1,2.,3.5,4])
# print(z)

class Car :
    fuel  = "Xăng"
    maxspeed = 150
    
    def drive(self):
        print('xe chay voi toc do :', self.maxspeed)

mini = Car()
# print(mini.drive())

class Student_1 :
    
    def info (self, name, age):
        print("Name : ", name , "Age : ", age )

jackson = Student_1()
# print(jackson.info("Thanh", 18))
class Student :
    def __int__(self,name,age) :
        print("Name : ",name, " Age: ",age)
    def __str__(self) :
        print('------')
thanh = Student('Nguyen Thanh',25)
print(thanh)