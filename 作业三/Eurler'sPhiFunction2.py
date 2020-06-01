def phi(n):
    a = 2
    phim = n
    num = []
    frac = []
    while(1):
        if n%a == 0:
            num.append(a)
        else:   ##更新因子
            a = a+1
            b = 2
            while(1): ##判断是否为素因子

                if a % b == 0:
                    a = a + 1
                    continue
                if b == a-1:
                    break
                b = b+1
            continue
        n=n // a
        if n == 1:
            break
    for i in num:
        long = 0
        leng = 0
        for l in range(len(num)):   #判断i是否为素因子列表当中的重复元素
            if i == num[l]:
               long = long+1
        if long == 1:      #若不重复，则进行累乘
            phim = phim * (1 - 1 / i)
        elif long > 1:      #若重复，则判断是否为第一次遇见
            for k in range(len(frac)):
                if i == frac[k]:
                    leng=leng + 1
            if leng == 0:   #若是第一次遇见，则进行累乘
                phim = phim * (1 - 1 / i)
                frac.append(i)

    return phim

print(phi(10))
