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

void makenum(int number[][4], int checknum[][4]); // 1���� 15���� 2���� �迭�� for���� �̿��� ����
void shuffle(int number[][4], int* x, int* y); // number�迭 ���� �������� ����
void makeboard(int map[][25]); // ������ ���� 0 : ���� , -1 : - , -2 : |
void printboard(int map[][25]); // number�迭 �������� ����� map�迭 ���
void inputnum(int map[][25], int number[][4]); // ���� ���� map�迭�� ����ֱ�
int checkcor(int *fx, int *fy); // Ű���� �Է��� * ������ǥ ���� number�迭�� ������� �׽�Ʈ (���ϰ��� 0�̸� �����۵� ���� 1�̸� �Ұ���)
void switchnum(int number[][4], int* x, int* y, int *fx, int *fy); // Ű���� �Է� �� ����� ��ǥ�� ���� number�迭���� ����
int finish(int number[][4], int checknum[][4]); // ���� ���� üũ 0 : ���� 1 : ����
void CursorView(); //Ŀ�������

int main()
{
	int map[13][25] = { { 0 } };
	int number[4][4]; // 1���� 15���� �������� �迭
	int checknum[4][4]; // ������ ������ 1���� 15���� ���ĺ񱳸����� �迭
	char ch;
	int x, y; // number�迭���� * ������ǥ ��
	int fx, fy; // * ������ǥ ��

	CursorView(); // Ŀ�������
	makenum(number, checknum); // 1���� 15���� 2���� �迭�� for���� �̿��� ����
	shuffle(number, &x, &y); // number�迭 ���� �������� ����
	makeboard(map); // ������ ����(shuffle�Լ����� �� number�迭 map�迭�� ����)
	fx = x;
	fy = y;
	
	while (1)
	{
		inputnum(map, number); // ���� ���� map�迭�� ����ֱ�
		printboard(map); // number�迭 �������� ����� map�迭 ���
		if (_kbhit)
		{
			ch = _getch();
			switch(ch) 
			{
			case LEFT:
				fx--;
				if (checkcor(&fx, &fy) == 1) fx++; // 1�̸� �۵��Ұ�
				else if (checkcor(&fx, &fy) == 0) // ���� �۵� ����
				{
					switchnum(number, &x, &y, &fx, &fy);
					x--;
				}
				break;
			case RIGHT:
				fx++;
				if (checkcor(&fx, &fy) == 1) fx--; // 1�̸� �۵��Ұ�
				else if (checkcor(&fx, &fy) == 0) // ���� �۵� ����
				{
					switchnum(number, &x, &y, &fx, &fy);
					x++;
				}
				break;
			case UP:
				fy--;
				if (checkcor(&fx, &fy) == 1) fy++; // 1�̸� �۵��Ұ�
				else if (checkcor(&fx, &fy) == 0) // ���� �۵� ����
				{
					switchnum(number, &x, &y, &fx, &fy);
					y--;
				}
				break;
			case DOWN:
				fy++;
				if (checkcor(&fx, &fy) == 1) fy--; // 1�̸� �۵��Ұ�
				else if (checkcor(&fx, &fy) == 0) // ���� �۵� ����
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
			inputnum(map, number); // ���� ���� map�迭�� ����ֱ�
			printboard(map);
			break;
		}
		system("cls");
	}
	
	printf("������ ���� �Ǿ����ϴ�.");
	return 0;
}

void makenum(int number[][4], int checknum[][4])
{
	int a = 0;

	for (int i = 0; i < 4; i++) // 1���� 15���� 2�����迭�� for���� �̿��� ����
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
			else if (map[i][j] == -1) printf("��");
			else if (map[i][j] == -2) printf("��");
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
	cursorInfo.dwSize = 1; //Ŀ�� ���� (1 ~ 100)
	cursorInfo.bVisible = FALSE; //Ŀ�� Visible TRUE(����) FALSE(����)
	SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursorInfo);
}