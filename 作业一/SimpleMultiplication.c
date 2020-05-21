#include <stdio.h>

int encode(int num)
{
    int a,b,c=1,d=0;
    while (1)
    {
        if(num==0)
        {
            return d;
        }
        a=num%2;
        d+=c*a;
        num/=2;
        c*=10;
    }
}

int mul(int e,int num)
{
    int x,total=0,i=0;
    while (1)
    {
        if(num==0)
        {
            return total;
        }
        x=num%10;
        total+=e*pow(2,i)*x;
        i++;
        num/=10;
    }
    
}

void main()
{
    int a,b;
    printf("Please Input a and b:");
    scanf("%d%d",&a,&b);
    printf("%d",mul(a,encode(b)));
    printf("\n");
    system("pause");
}
