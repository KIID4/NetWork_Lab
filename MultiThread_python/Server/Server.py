from socket import *
import threading
from queue import Queue


def Send(group, count, infor):
    print("Client %d 정보 전달 시작" % count)
    while True:
        try:
            recv = infor.get()  # recv[0] = 클라이언트 메세지, recv[1] = 메세지를 보낸 해당 클라이언트 , recv[2] = 클라이언트 번호
            if recv == 'new connection user':  # 새로운 클라이언트가 접속 할 경우 반복문을 종료하여 새로운 그룹 정보 갱신
                break

            for c_socket in group:
                msg = 'Client' + str(recv[2]) + ' >> ' + str(recv[0])
                if recv[1] != c_socket:  # 본인이 보낸 메세지는 출력 안함
                    c_socket.send(bytes(msg.encode()))

        except:
            pass


def Recv(c_socket, count, infor):
    print("Client %d 정보 수신 시작" % count)
    while True:
        data = c_socket.recv(1024).decode()
        infor.put([data, c_socket, count])  # 클라이언트 메세지, 메세지를 보낸 해당 클라이언트 소켓 정보, 클라이언트 번호


def main():
    infor = Queue()  # 정보 저장 큐
    HOST = ''  # 수신 받을 모든 IP를 의미
    PORT = 9000  # 수신 받을 Port
    s_socket = socket(AF_INET, SOCK_STREAM)  # TCP 소켓 생성 SOCK_STREAM // UDP 소켓 생성 SOCK_DGRAM
    s_socket.bind((HOST, PORT))  # 소켓에 수신받을 IP주소와 PORT를 설정
    s_socket.listen(10)  # 소켓 연결, 파라미터 = 클라이언트 접속 수를 의미
    count = 0  # 클라이언트 번호
    group = []  # 연결된 클라이언트 소켓 리스트

    while True:
        c_socket, addr = s_socket.accept()  # 해당 소켓을 열고 대기
        count = count + 1
        group.append(c_socket)  # 연결된 클라이언트의 소켓정보
        print('\nnew connection user')
        print('Connected ' + str(addr[0]))

        if count > 1:  # 새로운 클라이언트가 접속할 경우
            infor.put('new connection user')
            thread1 = threading.Thread(target=Send, args=(group, count, infor,))
            thread1.start()

        else:
            thread1 = threading.Thread(target=Send, args=(group, count, infor,))
            thread1.start()

        thread2 = threading.Thread(target=Recv, args=(c_socket, count, infor,))
        thread2.start()


if __name__ == '__main__':
    main()
