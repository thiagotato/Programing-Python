import socket

ip = '127.0.0.1'
port = 2222

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip, port))

s.listen(5)

while True:
    conn, addr = s.accept()
    conn.send('Bem vindo ao seu primeiro servidor TCP\n')
    print 'Conexao de %s:%d' %(addr[0], addr[1])
    conn.send('>>>')
    msg = conn.recv(1024)
    print 'Mensagem Recebiba: %s' %msg
    conn.close
    break
s.close()
