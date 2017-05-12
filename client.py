import threading
import paramiko
import subprocess
import sys

def ssh_command(ip, port, user, passwd, command):
    client = paramiko.SSHClient()
    #client.load_host_keys('/home/justin/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print ssh_session.recv(1024) #read banner
        while True:
            command = ssh_session.recv(1024) #get the command from the SSH server
            try:
                print "<<<", command
                ssh_session.send('received')
            except Exception,e:
                ssh_session.send(str(e))
                client.close()
    return

server = sys.argv[1]
port = int(sys.argv[2])

ssh_command(server, port, 'justin', 'lovesthepython','ClientConnected')
