def phi(n):
    num = 0
    for i in range(n):
        if i==0:
            continue
        if n%i != 0:
            num=num+1;
    return num+1

print(phi(8))