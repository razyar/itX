import os
import sys
from os import system 

filename = sys.argv[0]
sys.argv.append(1)
sys.argv.append(2)


if len(sys.argv) != 5:
	print 'Usage: %s username local_ip' % filename
	sys.exit('\n')


def domain_generator(username, ip):
	domain = '\n'+username+'\t'+ip
	f = open('/etc/hosts', 'a')
	f.write(domain)
	f.close()
	

try:
	domain_generator(str(sys.argv[1]), str(sys.argv[2]))
	print '[new itX username: ] http://%s@it.x ' % str(sys.argv[1])
except:
	sys.exit('[Error]: please run under sudo permission')