#!/usr/bin/env python
# coding: utf-8
# pwned-email v1.0
# By Leon Johnson - twitter.com/sho_luv

import requests
import sys
from pprint import pprint
from termcolor import colored, cprint

def hacked_email(email):
	request = "https://hacked-emails.com/api?q=%s" % (email)
	cprint("    checking https://hacked-emails.com",'white')
	r = requests.get(request)
	values = r.json()
	count = 0
	if values['results']:
		for list in values['data']:
			cprint('\t[+] ', 'red', attrs=['bold'], end='')  # print success
			cprint ("Found: %s in: %s " % (values['query'], values['data'][count]['title']), end='')
			cprint('(Pwn3d!)\n', 'yellow', attrs=['bold'], end='')  # print success
			count += 1

		return True
	else:
		cprint('\t[+] ', 'green', attrs=['bold'], end='')  # print success
		cprint ("Congrats: %s not found in dumps !" % (values['query']), end='\n')
		return False

def haveibeenpwned(email):
	request = "https://haveibeenpwned.com/api/v2/breachedaccount/%s" % (email)
	cprint("    checking https://haveibeenpwned.com",'white')
	r = requests.get(request)
	if r:
		values = r.json()
	else:
		values = 0
	#pprint( values)
	count = 0
	if values:
		for list in values:
			cprint('\t[+] ', 'red', attrs=['bold'], end='')  # print success
			cprint ("Found: %s in: %s " % (email, list['Name']), end='')
			cprint('(Pwn3d!)\n', 'yellow', attrs=['bold'], end='')  # print success
			count += 1

		return True
	else:
		cprint('\t[+] ', 'green', attrs=['bold'], end='')  # print success
		cprint ("Congrats: %s not found in dumps!" % (email), end='\n')
		return False

try:

	#if len(sys.argv) < 2:
	#	usage()
	email = sys.argv[1]

	found = 0
	if hacked_email(email):
		found = 1
	if haveibeenpwned(email):
		found = 1
	if found:
		print "\nSorry, don't shoot the messenger..."
	else:
		print "\nGreat Job!"

# except keyboard interrupt
except KeyboardInterrupt:
    print "[*] Okay, Okay... Exiting... Thanks for using pwned-emails.py"

