import pygame
import pyautogui
pyautogui.FAILSAFE = False  # 마우스 커서가 좌표 x = 0, y = 0으로 이동하면 프로그램을 종료하는 기능(안전장치) 비활성화
pygame.init()  # pygame 초기화

#==============================================================================================================
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# pygame 설정
screensize = [700, 500]  # 해상도 설정
screen = pygame.display.set_mode(screensize)  # pygame으로 생성할 창의 크기를 설정한 변수를 통해 GUI창 크기 설정
clock = pygame.time.Clock()  # 초당 화면을 몇번 출력하는지 (FPS)
numberFont = pygame.font.SysFont(None, 50)  # 숫자 글꼴 정의 (글꼴, 크기, 굵기 여부, 기울기 여부) None : 기본 글꼴
textFont = pygame.font.SysFont('malgungothic', 25)  # 한글 글꼴 정의
#==============================================================================================================


def Printboard():  # 게임판 출력
    for i in range(0, 256, 85):
        for j in range(0, 286, 85):
            pygame.draw.rect(screen, BLACK, [i, j, 90, 90], 4)  # 사각형 그리기 (화면선언 변수 값, 색, 좌표(x, y, 가로, 세로), 선 굵기)

    pygame.draw.rect(screen, BLACK, [480, 90, 150, 50], 4)  # 다시시작 판(사각형)출력
    pygame.draw.rect(screen, BLACK, [480, 150, 150, 50], 4)  # 게임종료 판(사각형)출력
    pygame.draw.rect(screen, BLACK, [80, 390, 150, 50], 4)  # 일시정지 판(사각형)출력

    text = textFont.render("일시정지", True, BLACK)
    screen.blit(text, [100, 400])
    text = textFont.render("움직인 횟수 : ", True, BLACK)
    screen.blit(text, [480, 40])
    text = textFont.render("다시 시작", True, BLACK)
    screen.blit(text, [500, 100])
    text = textFont.render("게임 종료", True, BLACK)
    screen.blit(text, [500, 160])
    text = textFont.render("걸린 시간 :     분     초", True, BLACK)  # 퍼즐을 풀때까지 걸린 시간
    screen.blit(text, [370, 400])

def drawtext(count, gameset, timecount=[], number=[]):  # 게임틀을 제외한 나머지 출력 ex) 1부터 15까지 출력
    x = 35  # 가장 기본이 되는 x좌표 출력
    y = 30  # 가장 기본이 되는 x좌표 출력

    for i in range(4):
        for j in range(4):
            if 10 <= number[i][j] <= 15:
                text = numberFont.render(str(number[i][j]), True, BLACK)  # (텍스트, 그래픽 기법, 색깔, 바탕색)
                screen.blit(text, [x - 10, y])  # blit함수를 이용해 텍스트를 출력 이미지와 흡사
                x += 85
            elif number[i][j] == 42:  # 빈칸
                text = numberFont.render(' ', True, BLACK)
                screen.blit(text, [x, y])
                x += 85
            else:
                text = numberFont.render(str(number[i][j]), True, BLACK)
                screen.blit(text, [x, y])
                x += 85
        y += 85
        x = 35

    text = numberFont.render(str(count), True, BLACK)
    screen.blit(text, [640, 42])
    text = numberFont.render(str(timecount[0]), True, BLACK)
    screen.blit(text, [500, 400])
    text = numberFont.render(str(timecount[1]), True, BLACK)
    screen.blit(text, [570, 400])
    text = numberFont.render(str(timecount[2]), True, BLACK)
    screen.blit(text, [640, 400])


    if gameset == 1:  # 퍼즐을 풀 경우
        text = textFont.render("축하합니다", True, BLACK)
        screen.blit(text, [500, 230])


def mousecor(vx, vy):  # 1 : 게임판 클릭(시작) 2 : 다시시작 3 : 게임종료 4: 일시정지
    check = 0

    if vx <= 340 and vy <= 340:
        check = 1
    elif (480 <= vx <= 630) and (90 <= vy <= 140):
        check = 2
    elif (480 <= vx <= 630) and (150 <= vy <= 200):
        check = 3
    elif (80 <= vx <= 230) and (400 <= vy <= 450):
        check = 4

    return check

def record():
    name = pyautogui.prompt(title='ID', text='ID를 입력하세요')

    return name