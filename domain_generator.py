import os

def new_domain(your_ip, your_domain):
	domain = your_ip+'\t\t'+your_domain
	f = open('/etc/hosts', 'a')
	f.write(domain)
	f.close()
	
	
new_domain('192.168.1.4', 'razyar@it.x')

