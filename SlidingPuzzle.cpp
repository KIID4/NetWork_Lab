#define _CRT_SECURE_NO_WRANINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
#include <conio.h>

#define UP 72
#define DOWN 80
#define LEFT 75
#define RIGHT 77

void makenum(int number[][4], int checknum[][4]); // 1부터 15까지 2차원 배열에 for문을 이용해 저장
void shuffle(int number[][4], int* x, int* y); // number배열 정보 무작위로 섞기
void makeboard(int map[][25]); // 게임판 생성 0 : 공백 , -1 : - , -2 : |
void printboard(int map[][25]); // number배열 정보까지 저장된 map배열 출력
void inputnum(int map[][25], int number[][4]); // 랜덤 숫자 map배열에 집어넣기
int checkcor(int *fx, int *fy); // 키보드 입력후 * 가상좌표 값이 number배열을 벗어나는지 테스트 (리턴값이 0이면 정상작동 가능 1이면 불가능)
void switchnum(int number[][4], int* x, int* y, int *fx, int *fy); // 키보드 입력 후 변경된 좌표에 대해 number배열에서 변경
int finish(int number[][4], int checknum[][4]); // 게임 종료 체크 0 : 종료 1 : 진행
void CursorView(); //커서지우기

int main()
{
	int map[13][25] = { { 0 } };
	int number[4][4]; // 1부터 15까지 정보저장 배열
	int checknum[4][4]; // 게임이 끝난후 1부터 15까지 정렬비교를위한 배열
	char ch;
	int x, y; // number배열내의 * 고정좌표 값
	int fx, fy; // * 가상좌표 값

	CursorView(); // 커서지우기
	makenum(number, checknum); // 1부터 15까지 2차원 배열에 for문을 이용해 저장
	shuffle(number, &x, &y); // number배열 정보 무작위로 섞기
	makeboard(map); // 게임판 생성(shuffle함수실행 후 number배열 map배열에 투입)
	fx = x;
	fy = y;
	
	while (1)
	{
		inputnum(map, number); // 랜덤 숫자 map배열에 집어넣기
		printboard(map); // number배열 정보까지 저장된 map배열 출력
		if (_kbhit)
		{
			ch = _getch();
			switch(ch) 
			{
			case LEFT:
				fx--;
				if (checkcor(&fx, &fy) == 1) fx++; // 1이면 작동불가
				else if (checkcor(&fx, &fy) == 0) // 정상 작동 가능
				{
					switchnum(number, &x, &y, &fx, &fy);
					x--;
				}
				break;
			case RIGHT:
				fx++;
				if (checkcor(&fx, &fy) == 1) fx--; // 1이면 작동불가
				else if (checkcor(&fx, &fy) == 0) // 정상 작동 가능
				{
					switchnum(number, &x, &y, &fx, &fy);
					x++;
				}
				break;
			case UP:
				fy--;
				if (checkcor(&fx, &fy) == 1) fy++; // 1이면 작동불가
				else if (checkcor(&fx, &fy) == 0) // 정상 작동 가능
				{
					switchnum(number, &x, &y, &fx, &fy);
					y--;
				}
				break;
			case DOWN:
				fy++;
				if (checkcor(&fx, &fy) == 1) fy--; // 1이면 작동불가
				else if (checkcor(&fx, &fy) == 0) // 정상 작동 가능
				{
					switchnum(number, &x, &y, &fx, &fy);
					y++;
				}
				break;
			}
		}
		if (finish(number, checknum) == 0)
		{
			system("cls");
			inputnum(map, number); // 랜덤 숫자 map배열에 집어넣기
			printboard(map);
			break;
		}
		system("cls");
	}
	
	printf("게임이 종료 되었습니다.");
	return 0;
}

void makenum(int number[][4], int checknum[][4])
{
	int a = 0;

	for (int i = 0; i < 4; i++) // 1부터 15까지 2차원배열에 for문을 이용해 저장
	{
		for (int j = 0; j < 4; j++)
		{
			number[i][j] = a;
			checknum[i][j] = a + 1;
			a++;
		}
	}

	number[0][0] = 42;
	checknum[3][3] = 42;
}

void makeboard(int map[][25])
{
	for (int i = 0; i < 25; i++)
	{
		map[0][i] = -1;
		map[3][i] = -1;
		map[6][i] = -1;
		map[9][i] = -1;
		map[12][i] = -1;
	}

	for (int i = 0; i < 13; i++)
	{
		map[i][0] = -2;
		map[i][6] = -2;
		map[i][12] = -2;
		map[i][18] = -2;
		map[i][24] = -2;
	}
}

void printboard(int map[][25])
{
	for (int i = 0; i < 13; i++)
	{
		for(int j = 0; j < 25; j++)
		{
			if (map[i][j] == 0) printf(" ");
			else if (map[i][j] == -1) printf("─");
			else if (map[i][j] == -2) printf("│");
			else if (map[i][j] == 42) printf("*");
			else if (map[i][j] >= 10)
			{
				printf("%d", map[i][j]);
				j++;
			}
			else printf("%d", map[i][j]);
		}
		printf("\n");
	}
}

void shuffle(int number[][4], int *x, int *y)
{
	int tmp;
	int a, b, c, d;
	srand((unsigned int)time(NULL));

	for (int i = 0; i < 100; i++)
	{
		a = rand() % 4;
		b = rand() % 4;
		c = rand() % 4;
		d = rand() % 4;

		tmp = number[a][b];
		number[a][b]= number[c][d];
		number[c][d] = tmp;
	}

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (number[i][j] == 42)
			{
				*x = j;
				*y = i;
			}
		}
	}
}

void inputnum(int map[][25], int number[][4])
{
	int a = 0;
	int b = 0;

	for (int i = 1; i < 13; i += 3)
	{
		for (int j = 3; j < 25; j += 6)
		{
			map[i][j] = number[a][b];
			b++;
		}
		a++;
		b = 0;
	}
}

int checkcor(int* fx, int* fy)
{
	int num = 0;
	int a = *fx;
	int b = *fy;
	
	if (a > 3 || a < 0 || b > 3 || b < 0) num = 1;

	return num;
}

void switchnum(int number[][4], int *x, int *y, int* fx, int* fy)
{
	int tmp;
	int a, b, i, j;
	
	a = *x;
	b = *y;
	i = *fx;
	j = *fy;

	tmp = number[b][a];
	number[b][a] = number[j][i];
	number[j][i] = tmp;
}

int finish(int number[][4], int checknum[][4])
{
	int num = 0, check = 0;

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (number[i][j] == checknum[i][j]) check++;
		}
	}
	
	if (check != 16) num = 1;

	return num;
}

void CursorView()
{
	CONSOLE_CURSOR_INFO cursorInfo = { 0, };
	cursorInfo.dwSize = 1; //커서 굵기 (1 ~ 100)
	cursorInfo.bVisible = FALSE; //커서 Visible TRUE(보임) FALSE(숨김)
	SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursorInfo);
}