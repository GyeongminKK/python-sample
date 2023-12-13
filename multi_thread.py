import socket
import threading
# 클라이언트 처리 스레드
class socket_multi_Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.stopRequest = threading.Event()
        self.socket_ip = "127.0.0.1"# ip 주소
        self.socket_port = int(1234) # port 주소
        self.web_lsn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.web_lsn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.web_lsn.bind((self.socket_ip, self.socket_port))
        self.web_lsn.listen()
    def run(self):
        while True:
            client_socket, addr = self.web_lsn.accept()
            print(f"클라이언트가 {addr}에서 연결되었습니다.")

            # 클라이언트를 처리하는 스레드 시작
            client_handler = threading.Thread(target=recv_msg, args=(client_socket,))
            client_handler.start()
def recv_msg(client_socket):
    while True:
        try:
            thread_id = threading.current_thread().ident
            recv_data = client_socket.recv(1024)
            print(f"Thread ID {thread_id}: 수신 응답: {recv_data.decode()}")
            client_socket.sendall(recv_data)
            if not recv_data:
                break

        except Exception as e:
            break

    print("클라이언트와의 연결 종료.")
    client_socket.close()


if __name__ == "__main__":
    socket_thread = socket_multi_Thread()
    socket_thread.start()
    socket_thread.join()