f = open('/home/vitalinya/ping1.text')
dict = {}
for line in f.readlines():
	
	if 'icmp_seq' in line:
		print (line)
		icmp_seq=(line.split()[4]).split('=')[1]
		time=(line.split()[6]).split('=')[1]
		dict['seq_'+ icmp_seq] = time

print(dict['seq_1001'])
f.close()