#include <stdlib.h>

int main()
{
    int sum1 = 0, sum2 = 0, i;
    for(i=1;i<101; i++)
    {
        sum1 += i*i;
        sum2 += i;
    }
    sum2 *= sum2;a
    return sum2-sum1;
}
