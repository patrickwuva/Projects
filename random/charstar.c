#include <stdio.h>
#include <stdlib.h>
#include <string.h>
size_t mystrlen(const char *s){
    
    int l = 0;
    while (s[l] != '\0'){
        l++;
    }
    return l;
}

char *simple_split(char *s, char delim){
    
    if(s == NULL || s[0] == '\0')
        return NULL;

    for (int i = 0; i < mystrlen(s); i++)
    {
        if(s[i] == delim){
            s[i] = '\0';
            return s+(i+1);
        }
    }

    return NULL;
}

int main(){
    char *trash, *bit, *s;
        trash = bit = s = strdup("can all aardvarks quaff?");
    do {
    s = bit;
    bit = simple_split(s, 'a');
    puts(s);
    } while(bit);
    free(trash);
    
    }
