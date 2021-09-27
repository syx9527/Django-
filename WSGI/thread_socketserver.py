import socket
import errno
import threading
import time

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''Hello world! <h1>邵曰信的WSGI第一个开发</h1> -from {thread_name}'''

response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sun,27 may 2018 01:01:01 GMT',
    'Content-Type: text/html; charset=utf-8',
    'Content-Length: {length}\r\n',
    body,
]

response = '\r\n'.join(response_params)


def handle_connection(conn, address):
    # print('oh,new conn', conn, address)
    # time.sleep(100)

    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)

    print(request)
    current_thread = threading.currentThread()
    content_length = len(body.format(thread_name=current_thread.name).encode())
    conn.send(response.format(thread_name=current_thread.name), length=content_length.encode())

    # conn.send(response.encode())  # response 转为bytes后传输
    conn.close()


def main():
    # socket.AF_INET  # 用于服务器与服务器之间的网络通信
    # socket.SOCK_STREAM  # 用于基于TCP的流式socket通信
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置端口可复用，保证我们每次按Ctrl+C组合键后，快速重启
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8000))
    serversocket.listen(10)  # 设置backlog--socket链接最大排队数量
    print("http://127.0.0.1:8000")
    serversocket.setblocking(0)  # 设置为非阻塞模式

    try:
        i = 0
        while True:
            try:
                conn, address = serversocket.accept()
            except socket.error as e:
                if e.args[0] != errno.EAGAIN:
                    raise
                continue
            i += 1
            print(i)
            t = threading.Thread(target=handle_connection, args=(conn, address), name="thread-%s" % i)
            t.start()
    finally:
        serversocket.close()


if __name__ == '__main__':
    main()
