import socket
import threading

client_addr = ('127.0.0.1',123)

def server_receive(server_socket):
    global client_addr  # 声明为全局变量
    # 接收数据
    while True:
        try:
            data, addr = server_socket.recvfrom(1024)
            client_addr = addr  # 更新全局变量
            print(f"Received from client {addr}: {data.decode()}")
        except Exception as e:
            #print(f"exception: {e}")
            a = 1
        
def server_send(server_socket):
    # 发送数据到客户端
    while True:
        send_message = input("请输入数据：")
        server_socket.sendto(send_message.encode(), client_addr)

def main():
    
    # 创建UDP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定IP地址和端口
    host = '127.0.0.1'
    port = 12345
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")
       
    try:
        receive_handler = threading.Thread(target=server_receive, args=(server_socket,))
        send_handler = threading.Thread(target=server_send, args=(server_socket,))
        
        receive_handler.start()
        send_handler.start()
    except Exception as e:
        print(f"error: {e}")

main()