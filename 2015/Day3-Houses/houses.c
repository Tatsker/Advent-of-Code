// Day 3 House Grid

#include <stdio.h>
#include <string.h>

int main(){
    int ArrGrid[500][500] = {0};

    int count(){
        FILE* fp = fopen("instructions.txt", "r");
        if(fp == NULL){
            printf("ERROR: Could not read file %s", "instructions.txt");
            return 1;
        }

        int x = 249;
        int y = 249;
        char instruction;

        while((instruction = fgetc(fp)) != EOF){
            if(instruction == '<'){
                x--;
            }else if(instruction == '>'){
                x++;
            }else if(instruction == '^'){
                y++;
            }else if(instruction == 'v'){
                y--;
            }else{
                printf("Error");
                return 0;
            }
            ArrGrid[y][x]++;
        }

        int num = 0;
        for (int i = 0; i < 500; i++)
        {
            for (int j = 0; j < 500; j++)
            {
                if (ArrGrid[i][j] > 0)
                {
                    num++;
                }
            }
        }

        printf("%i\n", num);
        fclose(fp);
        return 0;
    };
    
    int roboCount(){
        memset(ArrGrid, 0, sizeof ArrGrid);

        FILE* fp = fopen("instructions.txt", "r");
        if(fp == NULL){
            printf("ERROR: Could not read file %s", "instructions.txt");
            return 1;
        }

        int x = 149;
        int y = 149;
        int z = 149;
        int k = 149;
        char instruction;

        while((instruction = fgetc(fp)) != EOF){
            if(instruction == '<'){
                x--;
            }else if(instruction == '>'){
                x++;
            }else if(instruction == '^'){
                y++;
            }else if(instruction == 'v'){
                y--;
            }else{
                printf("Error");
                return 0;
            }
            ArrGrid[y][x]++;
            
            if((instruction = fgetc(fp)) != EOF){
                if(instruction == '<'){
                    z--;
                }else if(instruction == '>'){
                    z++;
                }else if(instruction == '^'){
                    k++;
                }else if(instruction == 'v'){
                    k--;
                }else{
                    printf("Error");
                    return 0;
                }
            }else{
                break;
            }
            ArrGrid[k][z]++;
        }

        int num = 0;
        for (int i = 0; i < 300; i++)
        {
            for (int j = 0; j < 300; j++)
            {
                if (ArrGrid[i][j] > 0)
                {
                    num++;
                }
            }
        }

        printf("%i\n", num);
        fclose(fp);
        return 0;
    };

    // Part 1
    int ret = count();

    // Part 2
    ret = roboCount();

    return 0;
}