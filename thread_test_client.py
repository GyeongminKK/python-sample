import socket
import threading
def send_data(port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', port))  # 서버의 IP 주소와 포트에 맞게 변경

    # 데이터 전송
    client_socket.sendall(message.encode())

    # 서버로부터 데이터 수신
    received_data = client_socket.recv(1024)
    print(f"서버 응답: {received_data.decode()}")

    # 소켓 닫기
    client_socket.close()


if __name__ == "__main__":
    # 서버 포트
    server_port = 12346  # 서버의 포트에 맞게 변경

    # 보낼 메시지
    message = "thread_test"

    # 여러 스레드에서 서버로 연결 및 데이터 전송
    thread_count = 20  # 스레드 개수
    threads = []

    for i in range(thread_count):
        thread = threading.Thread(target=send_data, args=(server_port, message))
        threads.append(thread)
        thread.start()

    # 모든 스레드가 종료될 때까지 대기
    for thread in threads:
        thread.join()

    print("모든 스레드가 종료되었습니다.")