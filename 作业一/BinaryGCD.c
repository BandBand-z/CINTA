#include <stdio.h>

int binarygcd(int a,int b)
{
    if(a<b)
    {
        int c;
        c=a;
        a=b;
        b=c;
    }
    if(b==0)
    {
        return a;
    }
    if((a&1)==0 && (b&1)!=0)
    {
        a>>=1;
        return binarygcd(a,b);
    }
    else if((a&1)!=0 && (b&1)==0)
    {
        b>>=1;
        return binarygcd(a,b);
    }
    else if((a&1)==0 && (b&1)==0)
    {
         a>>=1;
         b>>=1;
         return binarygcd(a,b);
    }
    else
    {   
        int d;
        d=a;
        a=b;
        b=d-b;
        return binarygcd(a,b);
    }
}

void main()
{
    int m=binarygcd(21,7);
    printf("%d",m);
    getchar();
}