import socket
import logging


# Checks for an active internet connection by connecting to Google's DNS server
def internet_check(host="8.8.8.8", port=53, timeout=3):
    while True:
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            logging.info("Internet connection verified.")
            break
        except socket.error as e:
            logging.error(e)
            pass
