import os
from os import system

def install_requires(rep):
	try:
		system('sudo apt-get install %s' % str(rep))
		print '[+] installing sucessfully for: %s' % str(rep)
	except Exception as insErr:
		print 'check this :\n %s' % str(insErr)

install_requires('apache2')
install_requires('php')
