#!/usr/bin/env python
# coding: utf-8
# pwned-email v1.0
# By Leon Johnson - twitter.com/sho_luv

import requests
import sys
from termcolor import colored, cprint

def hacked_email(email):
	request = "https://hacked-emails.com/api?q=%s" % (email)
	print request
	print 'cheaking https://hacked-emails.com'
	r = requests.get(request)
	#pprint( r.json())
	values = r.json()
	count = 0
	#print count
	if values['results']:
		for list in values['data']:
			cprint('\t[+] ', 'red', attrs=['bold'], end='')  # print success
			cprint ("Found: %s in: %s " % (values['query'], values['data'][count]['title']), end='')
			cprint('(Pwn3d!)\n', 'yellow', attrs=['bold'], end='')  # print success
			count += 1

		return True
	else:
		cprint('\t[+] ', 'green', attrs=['bold'], end='')  # print success
		cprint ("Congrats: %s has not been hacked!" % (values['query']), end='\n')
		return False
try:

	#if len(sys.argv) < 2:
	#	usage()
	email = sys.argv[1]


	if hacked_email(email):
		print "\nSorry, don't shoot the messenger..."
	else:
		print "\nGreat Job!"
# except keyboard interrupt
except KeyboardInterrupt:
    print "[*] Okay, Okay... Exiting... Thanks for using pwned-emails.py"

