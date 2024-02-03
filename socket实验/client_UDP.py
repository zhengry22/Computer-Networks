import socket
import threading

def client_send(client_socket, host, port):
    # 向服务器发送数据
    while True:
        send_input = input("请输入数据：")
        client_socket.sendto(send_input.encode('utf-8'), (host, port))

def client_receive(client_socket, host, port):
    # 接收服务器发送的数据
    while True:
        try:
            data, addr = client_socket.recvfrom(1024)
            print(f"Received from server {addr}: {data.decode()}")
        except Exception as e:
            #print(f"exception in client: {e}")
            a = 1

def main():
    print("main")
    
    # 创建UDP套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 服务器的IP地址和端口
    host = '127.0.0.1'
    port = 12345

    send_handler = threading.Thread(target=client_send, args=(client_socket, host, port))
    receive_handler = threading.Thread(target=client_receive, args=(client_socket, host, port), daemon=True)
    
    send_handler.start()
    receive_handler.start()
    

if __name__ == "__main__":
    main()
    # 关闭连接（UDP没有显式的连接和关闭连接的概念）
