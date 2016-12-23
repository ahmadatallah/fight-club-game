from socket import *
def server_test(current_object):

    s= socket(AF_INET,SOCK_STREAM)
    s.bind(("",1024))
    s.listen(5)
    print "server initialized"
#    while True:
    print "waiting for client"
    c,a = s.accept()
    print "recieved connection form",a
    c.send(str(current_object))
        #s.close()
