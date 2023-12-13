import socket
import threading
import select

class socket_Thread(threading.Thread):    
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.stopRequest = threading.Event()
        self.socket_ip = "127.0.0.1"# ip 주소
        self.socket_port = int(12346) # port 주소
        self.web_lsn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.web_lsn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.web_lsn.bind((self.socket_ip, self.socket_port))
        self.web_lsn.listen()
    def run(self):
        recv_msg(self.web_lsn)
        
def recv_msg(lsn):
    socket_list = [lsn,]  
    while True :
        try :
            read_sock, w, x = select.select(socket_list, [], [], 2)
            for sock in read_sock :
                if sock in [lsn, ] :
                    web_socket, addr = sock.accept()
                    if sock == lsn :
                        try:
                            thread_id = threading.current_thread().ident
                            recv_data = web_socket.recv(1024)
                            print(f"Thread ID {thread_id}: 수신 응답: {recv_data.decode()}")
                        except Exception as e:
                            web_socket.close()                            
        except Exception as error:
            web_socket.close()    
        
if __name__ == "__main__":    
    socket_thread = socket_Thread()
    socket_thread.start()
    socket_thread.join()