#include <stdio.h>

int min(int a,int b)
{
    if(a>b)
    {
        return b;
    }
    else
    {
        return a;
    }
    
}

int encode(int num)
{
    int r,times=1;
    long int binary=0;
    while (1)
    {
        r=num%2;
        num/=2;
        binary+=r*times;
        times*=10;
        if(num<2)
        {
            binary+=num*times;
            break;
        }
    }
    return binary;
}

int decode(int num){
    int decimal=0,i=0,r;
    while (1)
    {
        r=num%10;
        num/=10;
        decimal+=r*(pow(2,i));
        i++;
        if(num<2)
        {
            decimal+=num*(pow(2,i));
            break;
        }
    }
    return decimal;
}

int binarygcd(int a,int b)
{
    int gcd;
    int i=1;
    while(1)
    {
        if(b==0 && a!=0)
        {
            return decode(a)*i;
            break;
        }
        else if(a==0 && b!=0)
        {
            return decode(b)*i;
            break ;
        }
        
        if(a%10==0 && b%10==0)
        {
            a/=10;
            b/=10;
            i*=2;
        }
        else if(a%10==0 && b%10!=0)
        {
            a/=10;
        }
        else if(a%10!=0 && b%10==0)
        {
            b/=10;
        }
        else
        {
            int x=decode(a);
            int y=decode(b);
            x=abs(x-y);
            if(y>x)
            {
                a=encode(y);
                b=encode(x);
            }
            else
            {
                a=encode(x);
                b=encode(y);
            }                        
        }        
    }
}

void main()
{
    int a,b,gcd,a_binary,b_binary,gcd_binary;
    printf("Please Input a and b:");
    scanf("%d%d",&a,&b);
    a_binary=encode(a);
    b_binary=encode(b);
    // printf("a_binary:%d,b_binary:%d",a_binary,b_binary);
    // printf("\n");
    gcd_binary = binarygcd(a_binary,b_binary);
    gcd=gcd_binary;
    printf("The Greatest common divisor:%d",gcd);
    printf("\n");
    system("pause");
}