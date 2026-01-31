#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define N 9
int board[N][N];

void printBoard(int b[N][N]){
    int r,c;
    printf("   1 2 3   4 5 6   7 8 9\n");
    for(r=0;r<N;r++){
        if(r%3==0) printf("  +-------+-------+-------+\n");
        printf("%d |", r+1);
        for(c=0;c<N;c++){
            if(b[r][c]==0) printf(" .");
            else printf(" %d", b[r][c]);
            if((c+1)%3==0) printf(" |");
        }
        printf("\n");
    }
    printf("  +-------+-------+-------+\n");
}

bool usedInRow(int b[N][N], int row, int num){
    int c;
    for(c=0;c<N;c++) if(b[row][c]==num) return true;
    return false;
}

bool usedInCol(int b[N][N], int col, int num){
    int r;
    for(r=0;r<N;r++) if(b[r][col]==num) return true;
    return false;
}

bool usedInBox(int b[N][N], int boxStartRow, int boxStartCol, int num){
    int r,c;
    for(r=0;r<3;r++) for(c=0;c<3;c++) if(b[boxStartRow+r][boxStartCol+c]==num) return true;
    return false;
}

bool isSafe(int b[N][N], int row, int col, int num){
    return !usedInRow(b,row,num) && !usedInCol(b,col,num) && !usedInBox(b,row-row%3,col-col%3,num);
}

int randGen(int limit){
    return rand()%limit;
}

bool findUnassigned(int b[N][N], int *row, int *col){
    int r,c;
    for(r=0;r<N;r++) for(c=0;c<N;c++) if(b[r][c]==0){ *row=r; *col=c; return true; }
    return false;
}

bool fillBoard(int b[N][N]){
    int row,col;
    if(!findUnassigned(b,&row,&col)) return true;
    int nums[9];
    for(int i=0;i<9;i++) nums[i]=i+1;
    for(int i=8;i>0;i--){
        int j=randGen(i+1);
        int t=nums[i]; nums[i]=nums[j]; nums[j]=t;
    }
    for(int i=0;i<9;i++){
        int num=nums[i];
        if(isSafe(b,row,col,num)){
            b[row][col]=num;
            if(fillBoard(b)) return true;
            b[row][col]=0;
        }
    }
    return false;
}

void copyBoard(int src[N][N], int dst[N][N]){
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) dst[i][j]=src[i][j];
}

void removeKDigits(int b[N][N], int k){
    while(k>0){
        int cell = randGen(N*N);
        int r = cell / N;
        int c = cell % N;
        if(b[r][c]!=0){
            b[r][c]=0;
            k--;
        }
    }
}

bool isFull(int b[N][N]){
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) if(b[i][j]==0) return false;
    return true;
}

bool checkWin(int cur[N][N], int sol[N][N]){
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) if(cur[i][j]!=sol[i][j]) return false;
    return true;
}

bool validMove(int cur[N][N], int r, int c, int val){
    if(r<0||r>=N||c<0||c>=N) return false;
    if(cur[r][c]!=0) return false;
    return isSafe(cur,r,c,val);
}

void copyTo(int src[N][N], int dst[N][N]){
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) dst[i][j]=src[i][j];
}

int main(){
    srand(time(NULL));
    int full[N][N];
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) full[i][j]=0;
    fillBoard(full);
    int puzzle[N][N];
    copyBoard(full,puzzle);
    int removals = 45;
    removeKDigits(puzzle, removals);
    int current[N][N];
    copyBoard(puzzle,current);
    int sr, sc, sv;
    char cmd;
    printf("Simple Sudoku (enter h for help)\n");
    while(1){
        printBoard(current);
        if(checkWin(current,full)){
            printf("Congratulations! You solved the puzzle.\n");
            break;
        }
        printf("Enter command (i to insert, r to remove, h help, q quit): ");
        if(scanf(" %c",&cmd)!=1) break;
        if(cmd=='q') break;
        if(cmd=='h'){
            printf("i row col val (example: i 1 3 9)\n");
            printf("r row col (remove your entry)\n");
            printf("q quit\n");
            continue;
        }
        if(cmd=='i'){
            if(scanf("%d %d %d",&sr,&sc,&sv)!=3){ printf("invalid input\n"); while(getchar()!='\n'); continue; }
            sr--; sc--;
            if(sr<0||sr>=9||sc<0||sc>=9||sv<1||sv>9){ printf("out of range\n"); continue; }
            if(puzzle[sr][sc]!=0){ printf("cell is fixed\n"); continue; }
            if(validMove(current,sr,sc,sv)){
                current[sr][sc]=sv;
            } else {
                printf("move not allowed\n");
            }
            continue;
        }
        if(cmd=='r'){
            if(scanf("%d %d",&sr,&sc)!=2){ printf("invalid input\n"); while(getchar()!='\n'); continue; }
            sr--; sc--;
            if(sr<0||sr>=9||sc<0||sc>=9){ printf("out of range\n"); continue; }
            if(puzzle[sr][sc]!=0){ printf("cell is fixed\n"); continue; }
            current[sr][sc]=0;
            continue;
        }
        printf("unknown command\n");
    }
    return 0;
}