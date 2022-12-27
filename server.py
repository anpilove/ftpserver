import socket
import os
import shutil

dirname = os.path.join(os.getcwd(), 'docs')


def process(req):
    if req == 'pwd':
        return dirname
    elif req == 'ls':
        return '; '.join(os.listdir(dirname))
    elif 'cat' in req:
        nazv = req.split()[1]
        f = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), nazv))
        return f.read()
    elif 'mkdir' in req:
        nazv = req.split()[1]
        return os.mkdir(nazv)
    elif 'rmdir' in req:
        nazv = req.split()[1]
        return shutil.rmtree(nazv)
    elif 'remove' in req:
        nazv = req.split()[1]
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), nazv)
        return os.remove(path)
    elif 'rename' in req:
        nazv_star = req.split()[1]
        nazv_nov = req.split()[2]
        return os.rename(nazv_star, nazv_nov)
    else:
        return 'Может Вы ошиблись?'


PORT = 9097
sock = socket.socket()
sock.bind(('', PORT))
sock.listen()

while True:
    print("Прослушиваю порт: ", PORT)
    conn, addr = sock.accept()
    print(addr)
    request = conn.recv(1024).decode()
    print(request)
    response = process(request)
    if (request == 'pwd') or (request == 'ls') or ('cat' in request):
        conn.send(response.encode())
    elif ('mkdir' in request) or ('rmdir' in request) or ('remove' in request) or ('rename' in request):
        conn.send('Я сделал, как Вы просили.(Сервер)'.encode())
    else:
        conn.send(response.encode())