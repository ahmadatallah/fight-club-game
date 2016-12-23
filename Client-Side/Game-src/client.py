from socket import *
def client_test():
    s = socket(AF_INET,SOCK_STREAM)
    s.connect(("",1024))
#    while True:
    buf = s.recv(1000)
#        if len(buf) > 0:
#            print buf
#            break
    return buf
