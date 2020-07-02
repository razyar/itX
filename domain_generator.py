import os
import sys
from os import system 

filename = sys.argv[0]
sys.argv.append(1)
sys.argv.append(2)


if len(sys.argv) != 5:
	print 'Usage: %s username local_ip' % filename
	sys.exit('\n')

class generating:

	def domain_generator(self, username, ip):
		self.username = username
		self.ip = ip
		domain = '\n'+username+'\t'+ip
		f = open('/etc/hosts', 'a')
		f.write(domain)
		f.close()
	
	def qr_generator(self):
		try:
			system('qrencode -o qr.png http://%s@it.x' % self.username)
		except:
			print 'err'

generate = generating()

try:
	generate.domain_generator(str(sys.argv[1]), str(sys.argv[2]))
	print '[new itX username: ] http://%s@it.x ' % str(sys.argv[1])
except:
	sys.exit('[Error]: please run under sudo permission')

try:
	generate.qr_generator()
	system('xdg-open qr.png') #your itX qr
except Exception as qrerr:
	sys.exit('%s' % str(qrerr))