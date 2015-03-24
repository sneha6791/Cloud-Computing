#!/usr/bin/env python

import sys
import hashlib
import string

for line in sys.stdin:
    words = line.strip().lower().translate(None,string.punctuation).split()
    for w in words:
        h1 = hashlib.md5(w+'a').hexdigest()
        h2 = hashlib.md5(w+'b').hexdigest()	
        h3 = hashlib.md5(w+'c').hexdigest()
	n1 = int(h1,16)%1000000
	n2 = int(h2,16)%1000000
	n3 = int(h3,16)%1000000
	print '%s\t%s' % ('bloom',int(n1))
        print '%s\t%s' % ('bloom',int(n2))
	print '%s\t%s' % ('bloom',int(n3))
