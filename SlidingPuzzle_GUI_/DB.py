import mysql.connector

def getConnection():  # db 연결 함수
    config = {  # 연결할 DB의 정보 설정
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'database': 'pydb',  # 생성한 DB이름
        'port': '912'  # 포트번호
    }

    conn = mysql.connector.connect(**config)  # *이 1개면 인자가 튜플형식으로 전달,  *이 2개면 인자가 딕셔너리 형식으로 전달

    return conn


def create_table():  # 테이블 만드는 함수
    conn = getConnection()
    cur = conn.cursor()  # DB에 SQL문을 실행하거나 실행된 결과르 돌려받는 통로
    cur.execute('''  # execute 메소드를 이용하여 DB서버에 보냄
    create table gameinfo(  # 테이블 이름 생성
    name varchar(20),  # 변수 생성, 여기서 varchar은 파이썬에서의 문자열을 나타낸다
    movecon int,  
    minute int,
    second int,
    ms int)
    ''')
    conn.commit()  # DB적용
    conn.close()  # DB닫기


def checkname(name, count, timecount, cur):  # 이름이 테이블에 있는지 검사
    num = 0
    cur.execute('select * from gameinfo')
    check = cur.fetchall()
    for i in range(len(check)):
        if check[i][0] == name:
            num = 1
            break

    if num == 1:
        update_query = 'update gameinfo set movecon=%s, minute=%s, second=%s, ms=%s where name=%s'  # 정보 업데이트 SQL쿼리문
        cur.execute(update_query, (count, timecount[0], timecount[1], timecount[2], name))

    else:
        ins_query = 'insert into gameinfo values(%s,%s,%s,%s,%s)'  # 정보 입력 SQL쿼리문 생성
        cur.execute(ins_query, (name, count, timecount[0], timecount[1], timecount[2]))  # execute 메소드를 이용하여 DB서버에 보냄


def screcord(name, count, timecount):  # 점수 기록 메소드
    # create_table()  # 테이블이 없을경우 이 구문 실행
    conn = getConnection()
    cur = conn.cursor()
    checkname(name, count, timecount, cur)
    conn.commit()
    conn.close()



