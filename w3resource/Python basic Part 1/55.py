import netifaces

ifaces = netifaces.interfaces()

for iface in ifaces:
	iface_conf = netifaces.ifaddresses(iface)
	try:
		print(iface,'ipv4 =',iface_conf[netifaces.AF_INET][0]['addr'])
	except KeyError:
		print(iface,'does not have ipv4 address')
		pass
