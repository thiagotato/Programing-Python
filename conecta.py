import socket
import sys

host = sys.argv[1]
path = sys.argv[2] if len(sys.argv) >= 3 else ''

msg = 'GET /%s HTTP/1.1\nHost: %s\n\n' % (path, host)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

print 'conectando'
s.connect((socket.gethostbyname(host), 80))

print 'Enviando'
s.send(msg)

print 'Recebendo'
data = ''
while 1:
    try:
        buf = s.recv(1024)
        data += buf
    except Exception as e:
        break
print data    
