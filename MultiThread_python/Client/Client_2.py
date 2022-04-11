from socket import *
import threading


def Send(c_socket):
    while True:
        try:
            send_data = input().encode()  # 사용자 입력
            c_socket.send(send_data)  # Client -> Server 데이터 송신

        except:
            break


def Recv(c_socket):
    while True:
        try:
            recv_data = c_socket.recv(1024).decode()  # Server -> Client 데이터 수신
            print(recv_data)

        except:
            print('서버와의 연결이 끊겼습니다.')
            break


def main():
    c_socket = socket(AF_INET, SOCK_STREAM)  # TCP Socket
    Host = 'localhost'  # 통신할 대상의 IP 주소
    Port = 9000  # 통신할 대상의 Port 주소
    c_socket.connect((Host, Port))  # 서버로 연결시도
    print('서버에 접속하였습니다')

    # 메세지를 보낼 쓰레드
    thread1 = threading.Thread(target=Send, args=(c_socket,))
    thread1.start()

    # 서버로부터 other client의 메세지를 받을 쓰레드
    thread2 = threading.Thread(target=Recv, args=(c_socket,))
    thread2.start()



if __name__ == '__main__':
    main()
