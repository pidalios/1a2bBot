#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void pida_random(char *filename);
void pida_guess(char *filename, char *guess);
void pida_close(char *filename);

int main(int c, char **args){
    char *cmd = args[1];
    char *who = args[2];
    char *num = args[3];
    if(strcmp("start", cmd) == 0){
        pida_random(who);
    } else if(strcmp("guess", cmd) == 0){
        pida_guess(who, num);
    } else if(strcmp("close", cmd) == 0){
        //pida_close(who);
    }
    return 0;
}

void pida_random(char *filename){
    char real[10]={'0','1','2','3','4','5','6','7','8','9'};
    srand(time(NULL));
    int k;

    for(int i=0;i<10;i++)
    {
        k=rand()%10;
        char tmp;
        tmp=real[i];
        real[i]=real[k];
        real[k]=tmp;
    }
    
    FILE *pf;
    if((pf = fopen(filename, "w")) == NULL){
        return;
    }
    
    fprintf(pf,"%c%c%c%c",real[0],real[1],real[2],real[3]);
    
    fclose(pf);
    
}

void pida_guess(char *filename, char *guess){
    char realnum[4];
    int counterA=0, counterB=0;
    FILE *pf;
    if((pf = fopen(filename, "r")) == NULL){
        return;
    }
    fscanf(pf, "%c%c%c%c" ,&realnum[0],&realnum[1],&realnum[2],&realnum[3]);
    
    fclose(pf);
    
    for(int i=0; i<4; i++){
        if(realnum[i] == guess[i])
        counterA++;
        for(int j=0; j<4; j++){
            if(realnum[i] == guess[j] && i != j)
            counterB++;
        }
    }
    
    printf("%c%c%c%c    %dA%dB",guess[0],guess[1],guess[2],guess[3],counterA,counterB);
    
    if(counterA == 4){
        printf("You win!\nEnter /start to start the game");
        return;
    } 
}
