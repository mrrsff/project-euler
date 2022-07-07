#include <stdlib.h>
#include <math.h>

int isPrime(int x)
{
    int i=5, stop = sqrt((double)x);
    if(x%2==0) return 0;
    if(x%3==0) return 0;
    while(i <= stop)
    {
        if(x%i==0 || x%(i+2)==0) return 0;
        i+=6;
    }
    return 1;
}

int main()
{
    int i=13, primeCount=5, lastPrime;
    while(primeCount<10001)
    {
        if(isPrime(i))
        {
            primeCount++;
            lastPrime = i;
        }
        i++;
    }
    return lastPrime;
}
