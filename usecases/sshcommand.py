#!/usr/bin/python3

import paramiko

host = '192.168.44.11'
user = 'sadmin'
secret = 'P@ssw0rd'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host,username=user,password=secret,port=port)
stdin,stdout,stderr = client.exec_command('ls -la')
data = stdout.read() + stderr.read()
print(data,sep=' ',end='\n')
client.close()