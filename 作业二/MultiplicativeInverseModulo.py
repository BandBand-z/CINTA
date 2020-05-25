def gcd(a,b):
    if(b>a):
        c=a
        a=b
        b=c
    while(b):
        c = a
        a = b
        b = int(c) % int(a)
    return a

def egcd(a,b):
    if(b==0):
        return a,1,0
    r,x,y = egcd(b,int(a)%int(b))
    z=y
    y=x-(int(a)//int(b))*int(y)
    x=z
    return r,x,y

print("请输入a:")
a = input()
print("请输入n:")
n = input()
if(gcd(a,n)!=1):
    print("所输入的a和n不是互素，两者的乘法逆元无解")
r,x,y = egcd(a,n)
print("a模n的乘法逆元为："+str(x))