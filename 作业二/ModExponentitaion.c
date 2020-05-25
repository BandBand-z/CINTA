#include <stdio.h>

// 使用迭代完成模指数运算
int ModExp(int x,int y,int m)
{
    int sum;
    for(int i=1;i<=y;i*=2)
    {
        if(i==1) //判断是否为第一项,若是进行单独的运算
        {
        sum=(int)x%(int)m;
        }
        else //若不是第一项则直接进行幂乘运算
        {
        sum=(int)pow(sum,2)%(int)m;
        }
    }
    if(y&1==1) //判断指数是否为奇数，若是则再乘一次
    {
        sum=(int)(x*sum)%(int)m;
    }
    return sum;
}

void main()
{
    int x,y,m;
    printf("Please input the value of x,y,z:");
    scanf("%d%d%d",&x,&y,&m);
    printf("the result of x^y mod m:%d",ModExp(x,y,m));
    printf("\n");
    system("pause");
}