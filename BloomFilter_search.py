#!/usr/bin/env python

import sys
import hashlib
import string

for line in file(sys.argv[1],'r'):
	bfilter = line

	while(True):
		inputstr = raw_input("Search Word:")
		h1 = hashlib.md5(inputstr+'a').hexdigest()
		h2 = hashlib.md5(inputstr+'b').hexdigest()
		h3 = hashlib.md5(inputstr+'c').hexdigest()
		n1 = int(h1,16)%1000000
		n2 = int(h2,16)%1000000
		n3 = int(h3,16)%1000000
		if(bfilter[n1] == '1' and bfilter[n2] == '1' and bfilter[n3] == '1'):
			print "Found!"
		else:
			print "Not found!Try again."
		if inputstr == "exit":
			exit()
