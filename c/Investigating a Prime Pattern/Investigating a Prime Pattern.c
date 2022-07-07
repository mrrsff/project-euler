#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

#define ACCURACY 10

int miller_rabin(long long int, long long int), isPrime(long long int);
long long int power(long long int,long long int,long long int);
int main()
{
    srand(time(NULL));
    long long int count=0, i, sum=0, square;
    i = 315410;
    square = i*i;
    printf("%d", isPrime(square+1));
    for(i=10;i<1000000;i+=10)
    {
        square = i*i;
        if(i%3 && i%7 && i%13 && isPrime(square+1) && isPrime(square+3) && isPrime(square+7) && isPrime(square+9) && !isPrime(square+11) && isPrime(square+13) && !isPrime(square+17) && !isPrime(square+21)
    && !isPrime(square+23) && isPrime(square+27))
        {
            sum+=i;
            printf("count:%lld, num:%lld, sum:%lld\n",++count,i,sum);
        }
    }
    return 0;
}
long long int power(long long int a, long long int d, long long int n)
{
    long long int res=1;
    while(d)
    {
        if(d & 1) res = (res*a) % n;
        d = d >> 1;
        a = (a*a) % n;
    }
    return res;
}
int miller_rabin(long long int n, long long int d)
{
    long long int a, i, x;
    a = 2 + rand() % (n-4);
    x = power(a, d, n);

    if(x==1 || x==n-1) return 1;
    while(d!=n-1)
    {
        x = (x*x) % n;
        d = d << 1;
        if(x==n-1) return 1;
        if(x==1) return 0;
    }
    return 0;
}

int isPrime(long long int n)
{
    int i;
    long long int temp;
    temp = n-1;
    while(!(temp&1))
    {
        temp = temp >> 1;
    }
    for(i=0;i<ACCURACY;i++)
    {
        if(!miller_rabin(n, temp)) return 0;
    }
    return 1;
}
