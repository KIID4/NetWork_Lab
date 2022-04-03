import os, time
from SlidingPuzzle_GUI_.pygameGUI import *
from SlidingPuzzle_GUI_.Gamecontent import*
from SlidingPuzzle_GUI_.DB import *
cls = lambda: os.system('cls')

def main():
    number = [[0] * 4 for i in range(4)]
    count = 0  # 도형 움직임 카운트 변수
    x = 0  # 빈칸의 x 좌표
    y = 0  # 빈칸의 y 좌표
    timecount = [0] * 3  # time[0] = 분(M) time[1] = 초(s) time[2] = 밀리초(ms)
    gameset = 0  # 퍼즐 클리어 체크 변수 0 : 진행 1: 클리어
    restart = 0  # 게임 재시작 체크 변수 0 : 재시작 1: 진행
    pause = 0  # 게임 일시정지 체크 변수 0 : 진행 1: 정지

    while True:
        if restart == 0:  # 다시시작 버튼을 클릭할 경우 restart = 0
            remixnum(number)
            x, y = check(number)
            restart += 1

        clock.tick(40)  # 초당 프레임
        screen.fill(WHITE)  # 화면을 (색)으로 채움
        Printboard()
        drawtext(count, gameset, timecount, number)  # 게임틀을 제외한 나머지 출력 ex) 1부터 15까지 출력
        event = pygame.event.poll()  # 이벤트 값 반환 하여 event.type에 저장 ex) 마우스 클릭

        if event.type == pygame.QUIT:  #pygame.QUIT는 GUI상에서 우측 상단 X를 나타냄
            break

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # pygame.MOUSEBUTTONDOWN : 클릭  / event.button == 1 왼쪽 == 2 휠 == 3 오른쪽
            vx = event.pos[0]  # x좌표 값
            vy = event.pos[1]  # y좌표 값
            if mousecor(vx, vy) == 1 and gameset == 0 and pause == 0:  # 게임판을 클릭하였을 때
                vx //= 90  # 퍼즐판의 크기를 마우스가 클릭한 시점의 좌표에서 나눠 몫만 따로 뗌(x 좌표)
                vy //= 90  # 퍼즐판의 크기를 마우스가 클릭한 시점의 좌표에서 나눠 몫만 따로 뗌(y 좌표)
                if checkcor(x, y, vx, vy) == 1: # 마우스 좌표를 이용하여 충돌 여부 검사 0 : 충돌 1 : 정상작동
                    switchnum(x, y, vx, vy, number)
                    x = vx
                    y = vy
                    count += 1
                screen.fill(WHITE)

                if finish(number) == 0:  # 게임이 끝났는지 체크
                    screen.fill(WHITE)
                    Printboard()  # 게임판 출력
                    drawtext(count, gameset, timecount, number)  # 게임틀을 제외한 나머지 출력 ex) 1부터 15까지 출력
                    gameset = 1
                    name = record()
                    screcord(name, count, timecount)

            elif mousecor(vx, vy) == 2:  # 다시시작의 경우 모든 변수를 초기화 후 실행
                gameset = 0
                count = 0
                restart = 0
                timecount = [0] * 3
                pause = 0

            elif mousecor(vx, vy) == 3:  # 게임종료의 경우 무한반복문을 만들어 탈출
                break

            elif mousecor(vx, vy) == 4:  # 일시정지의 경우 일시정지 버튼을 누른후에 게임진행 x 한번더 눌러야 게임진행 o
                pause += 1
                if pause == 2:
                    pause = 0

        if gameset == 0 and pause == 0:  # 퍼즐이 클리어 되지 않을 경우 않고 일시정지가 되지 않앗을 경우
            timecount[2] += 1
            if timecount[2] > 38:
                timecount[1] += 1
                timecount[2] = 0
            elif timecount[1] > 60:
                timecount[0] += 1
                timecount[1] = 0

        pygame.display.update()  # 화면에 작성한 모든 행위들을 업데이트해주기 위함


if __name__ == '__main__':
    main()
