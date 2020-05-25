# 欧几里得算法
def gcd(a,m):
    if m==0 :
        return a
    else:
        return gcd(m,int(a)%int(m))

# 扩展欧几里得算法
def egcd(a,m):
    if m == 0:
        return a,1,0
    r,x,y = egcd(m,int(a)%int(m))
    z=x
    x=y
    y=z-(int(a)//int(m))*int(y)
    return r,x,y

def congruence(a,b,m):
    i=0;
    if gcd(a,m)==1 and b==1: # 首先判断a和m是否互素以及b是否为1，若是直接返回a与m的乘法逆元
        r,x,y =egcd(a,m)
        return x
    elif gcd(a,m)==1: # 若b不为1，则返回b乘a与m的乘积
        r, x, y = egcd(a,m)
        return b*int(x)
    else:   # 若a与m不互素，则遍历摸的一个完全剩余系进行求解
        result = []
        while(i<14):
            if int(a*i)%int(m) == b:
                result.append(i)
            i=i+1
        return result

print("Please input the values of a,b,m:")
a=input()
b=input()
m=input()
result = congruence(a,b,m)
print(result)



