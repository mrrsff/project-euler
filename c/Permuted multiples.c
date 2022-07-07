#include <stdlib.h>
#include <string.h>

int sameCharacters(char *word1, char *word2)
{
    int i, j, count=0;
    char *tempWord1, *tempWord2;
    tempWord1 = word1;
    tempWord2 = word2;
    for(i=0; tempWord1[i]; i++)
    {
        for(j=0; tempWord2[j]; j++)
        {
            if(tempWord1[i]==tempWord2[j])
            {
                tempWord1[j]='#';
                count++;
            }
        }
    }
    return count;
}

int main()
{
    int i,num = 10, upper_bound=1000000;
    char converted[6][20], word1[]= "123456", word2[]="654321";
    while(num++<upper_bound)
    {
        for(i = 1; i<=6;i++){sprintf(converted[i-1], "%d", num*i);}
        if(sameCharacters(converted[0],converted[1])== strlen(converted[0]))
        {
            printf("NUM is: %d\nword1: %s\nword2: %s\nstrlen(converted[0])= %d\nsameCharacters(converted[0],converted[1])= %d", num, converted[0],converted[1], strlen(converted[0]), sameCharacters(converted[0],converted[1]));
            return num;
        }
    }
    return 0;
}
