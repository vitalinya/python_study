#!/usr/bin/python3
import paramiko
import nmap
import sys

hosts = sys.argv[2]
command = sys.argv[1]

nm = nmap.PortScanner()

ip_range = nm.scan(hosts=hosts,arguments='-sP')

user = 'cumulus'
secret = 'P@ssw0rd'
port = 22

for host in ip_range['scan']:

	print('host =', host)
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname=host,username=user,password=secret,port=port)
	stdin,stdout,stderr = client.exec_command(command)
	stdin.close()
	data = stdout.read() + stderr.read()
	print(data.decode())
	client.close()