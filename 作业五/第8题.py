def phi(a): #进行欧拉函数的计算
    n = 1
    i = 0
    while n < int(a) :
        if int(a)%n != 0:
            i=i+1
        n=n+1
    return i+1


def findgenerator(p):   #找出可能的生成元
    i = 1
    n = 0
    list = []
    maybegen = []
    while i < int(p):
        list.append(i)
        i=i+1;
    while n< int(p)-1:
        if (list[n]==1):
            n=n+1
            continue
        if ((list[n]**(int(p)-1))%int(p))==1:   #预先判断条件，元素的群阶次运算看结果是否为单位元
            maybegen.append(list[n])
            n=n+1
    return maybegen

def realgenerator(list,p):  #再根据预先筛选出来的单位元进行进一步的筛选
    generator2 = []
    i = 0
    while i< len(list):
        n = 1
        generator = []
        while n < int(p) :
            generator.append((list[i]**n)%int(p))   #通过对可能是生成元的元素进行对接阶次的运算
            n=n+1
        generator1=set(generator)   #去除重复的元素
        if len(generator1)==int(p)-1:   #与群阶进行对比，若生成子群的阶与群阶一致，则该元素是生成元
            generator2.append(list[i])
        i = i+1
    return generator2

privitenumber = input("请输入一个素数：")
generator = realgenerator(findgenerator(privitenumber),privitenumber);
print("Z_p*的一个生成元为："+str(generator))
