import random

def jugdep(p):  #判断是否为素数
    i = 2
    n = 1
    while i <int(p) :
        if int(p)%i ==0 :
            n=0
            break
        i = i + 1
    return n

def group(p):   #生成Z_p*
    list = []
    n=1
    while n < int(p) :
        list.append(n)
    return list

def findg(group,p): #找到g
    h = random.randint(2,int(p)-1)
    g = ((group[h])**2)%p
    return g

def gergroup(g,p):  #生成子群<g>
    q = (int(p)-1)//2
    i = 1
    generator = []
    while i <= q :
        generator.append((int(g)**i)%p)
    return generator

q = input("请输入一个素数q:")
p = 2*q+1
list = gergroup(findg(group(p),p),p)
print("生成群<g>为：")
print(list)