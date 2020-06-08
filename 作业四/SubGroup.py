import random

def Group(p):    #生成群
    group = []
    p = p-1
    while(1):
        if p>0:
            group.append(p)
            p = p - 1
        elif p == 0:
            break
    return group

def SubGroup(p,group=[]):  #生成子群
    subgroup = random.sample(group, random.randint(1, len(group)))
    return subgroup

def SquareSubGroup(p,group=[]):  #生成二次子群
    squaregroup = []
    i = 0
    while(1):
        if i< len(group):
            squaregroup.append(pow(group[i],2)%p)
            i = i+1
        elif i == len(group):
            break
    return list(set(squaregroup))

def CubicSubGroup(p,group=[]):   #生成三次子群
    cubegroup = []
    i = 0
    while(1):
        if i< len(group):
            cubegroup.append(pow(group[i],2)%p)
            i = i+1
        elif i == len(group):
            break
    return list(set(cubegroup))

number = 13
group1 = Group(number)
group2 = SubGroup(number,group1)
group3 = SquareSubGroup(number,group2)
group4 = CubicSubGroup(number,group3)

print("普通群：" + str(group1) +"其阶为：" + str(len(group1)))
print("一次子群:"+str(group2) + "其阶为：" + str(len(group2)))
print("二次子群:"+str(group3) + "其阶为：" + str(len(group3)))
print("三次子群:"+str(group4) + "其阶为：" + str(len(group4)))

# 发现的规律：
# 一次子群与原群的阶没有什么关系，二次子群、三次子群与原群的关系为：二次子群、三次子群的阶可以整除原群的阶