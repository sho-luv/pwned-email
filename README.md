# DEPRECATED

```diff
- Note: No longer works as haveIbeenpwned.com has switched to a paid for service. -
```

# Pwned-email

This is a command line tool that checks to see if the passed email has been part of a known compromise dump of data. It uses API calls from the websites:
- https://hacked-emails.com/
- https://haveibeenpwned.com/

The main goal of this was to have a way to check these sites from the command line.

## Install dependencies to get it to work
```
$ pip install requests
```

## Example output email not found in dumps:

```
./pwned-email.py administrator@fake.com
    checking https://hacked-emails.com
	[+] Congrats: administrator@fake.com not found in dumps !
    checking https://haveibeenpwned.com
	[+] Congrats: administrator@fake.com not found in dumps!

Great Job!

```

## Eample output of email found in lots of dumps:
```
./pwned-email.py administrator@gmail.com
    checking https://hacked-emails.com
	[+] Found: administrator@gmail.com in: evony.com (Pwn3d!)
	[+] Found: administrator@gmail.com in: btsec.com (Pwn3d!)
	[+] Found: administrator@gmail.com in: netease.com (Pwn3d!)
	[+] Found: administrator@gmail.com in: MongoDB Crawlers Pack sensmail.com KR (Pwn3d!)
	[+] Found: administrator@gmail.com in: oneclickroot.com (Pwn3d!)
	[+] Found: administrator@gmail.com in: Youtubers Database (Pwn3d!)
	[+] Found: administrator@gmail.com in: leet.cc (Pwn3d!)
	[+] Found: administrator@gmail.com in: exploit.in (compilation) (Pwn3d!)
	[+] Found: administrator@gmail.com in: Unknown Dumps Database (Pwn3d!)
	[+] Found: administrator@gmail.com in: Unknown Database FR (Pwn3d!)
	[+] Found: administrator@gmail.com in: Dump 66k Email Pass (Pwn3d!)
	[+] Found: administrator@gmail.com in: Unknown Dump (Pwn3d!)
	[+] Found: administrator@gmail.com in: 100k Email:plaintext dump (Pwn3d!)
	[+] Found: administrator@gmail.com in: 000webhost.com (Pwn3d!)
	[+] Found: administrator@gmail.com in: GMail Big Dump (Pwn3d!)
	[+] Found: administrator@gmail.com in: Adobe Users (Pwn3d!)
	[+] Found: administrator@gmail.com in: imesh.com (Pwn3d!)
	[+] Found: administrator@gmail.com in: MySpace (Pwn3d!)
	[+] Found: administrator@gmail.com in: Dropbox (Pwn3d!)
    checking https://haveibeenpwned.com
	[+] Found: administrator@gmail.com in: 000webhost (Pwn3d!)
	[+] Found: administrator@gmail.com in: Adobe (Pwn3d!)
	[+] Found: administrator@gmail.com in: BTSec (Pwn3d!)
	[+] Found: administrator@gmail.com in: Dropbox (Pwn3d!)
	[+] Found: administrator@gmail.com in: Edmodo (Pwn3d!)
	[+] Found: administrator@gmail.com in: Evony (Pwn3d!)
	[+] Found: administrator@gmail.com in: iMesh (Pwn3d!)
	[+] Found: administrator@gmail.com in: Leet (Pwn3d!)
	[+] Found: administrator@gmail.com in: MySpace (Pwn3d!)
	[+] Found: administrator@gmail.com in: RiverCityMedia (Pwn3d!)
	[+] Found: administrator@gmail.com in: VK (Pwn3d!)

Sorry, don't shoot the messenger...
```
