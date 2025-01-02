import socket


def internet_check(host="8.8.8.8", port=53, timeout=3):
    while True:
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            print("Connection successful")
            break
        except socket.error as e:
            print(e)
            pass
