import sys
import hashlib
import string

bloom = []
for i in range(1000000):
	bloom.append(0)
for line in sys.stdin:
	(key,val) = line.split('\t')
        bloom[int(val)] = 1

strng = ''.join(str(e) for e in bloom)
print strng
