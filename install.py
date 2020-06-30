import os
from os import system

def install():
	try:
		system('cp ./data/index.html /var/www/html')
		system('cp ./data/up.php /var/www/html')
		print 'now generate an domain and use it.'
	except Exception as installingerr:
		print 'Check: %s' % str(installingerr)

install()