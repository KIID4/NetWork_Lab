import random

def remixnum(number):
    tmp = 0
    a = 0
    randomarr = []

    """for i in range(16):
        randomarr.append(i)

    randomarr[0] = 42  # 42의 아스키 코드 : *
    random.shuffle(randomarr)

    for i in range(4):
        for j in range(4):
            number[i][j] = randomarr[a]
            a += 1"""


    for i in range(1, 17):  # 게임 종료 테스트 용 코드드
        randomarr.append(i)

    randomarr[14] = 42  # 42의 아스키 코드 : *
    randomarr[15] = 15

    for i in range(4):
        for j in range(4):
            number[i][j] = randomarr[a]
            a += 1


def checkcor(x, y, vx, vy):  # 마우스 좌표를 이용하여 충돌 여부 검사 0 : 충돌 1 : 정상작동
    check = 0

    if (vx + 1 == x and vy == y) or (vx - 1 == x and vy == y) or (vx == x and vy + 1 == y) or (vx == x and vy - 1 == y):
        if vx <= 3 or vx >= 0 or vy <= 3 or vy >= 0:
            check = 1

    return check


def switchnum(x, y, vx, vy, number=[]):
    tmp = 0

    tmp = number[y][x]
    number[y][x] = number[vy][vx]
    number[vy][vx] = tmp


def finish(number=[]):  # 게임이 끝났는지 체크
    num = 0  # num값을 리턴함으로써 끝났는지 체크 0 : 게임 끝 1 : 게임 진행
    check = 0
    checknum = [[0] * 4 for i in range(4)]
    a = 0

    for i in range(4):
        for j in range(4):
            checknum[i][j] = a + 1
            a += 1

    checknum[3][3] = 42

    for i in range(4):
        for j in range(4):
            if number[i][j] == checknum[i][j]:
                check += 1

    if check != 16:
        num = 1

    return num

def check(number = []):

    for i in range(4):
        for j in range(4):
            if number[i][j] == 42:
                return j, i