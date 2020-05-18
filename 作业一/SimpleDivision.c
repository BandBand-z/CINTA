#include <stdio.h>

int * divide(int a,int b){   
    static int result[2];
    {    
        if(a==0)
        {
            result[0]=0;
            result[1]=0;
            return result;
        }
        divide(a/2,b);
        int q=result[0];
        int r=result[1];
        q*=2;
        r*=2;
        if (a&1)
        {
            r=r+1;
        }
        if(r>=b)
        {
            r=r-b; 
            q=q+1;
        }
        result[0]=q;
        result[1]=r;
    }
    return result;
}

void main()
{
    int array[2];
    int *r;
    printf("Please Input a and b:");
    scanf("%d%d",&array[0],&array[1]);
    r = divide(array[0],array[1]);
    printf("q:%d",*(r));
    printf(" ");
    printf("r:%d",*(r+1));
    printf("\n");
    system("pause");
}