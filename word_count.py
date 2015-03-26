import mincemeat
import sys
import math
import re
import string

f = open(sys.argv[1],'r')
data = list(f)
length = len(data)
f.close()

punc = string.punctuation
input_list = []
count = 1
old_line = ''
for line in file(sys.argv[1]):
    line = line.lower()
    line = line.translate(None, punc)
    if count % length == 0:
        input_list.append((old_line+line).replace('\n',' '))
        old_line = ''
    else:
        old_line= old_line+line
    count+=1



datasource = dict(enumerate(input_list))


def mapfn(k,v):
    for w in v.split():
        yield w, 1
                
def reducefn(k,vals):
    return sum(vals)
    
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
i = 0
for k in sorted(results, key=results.get, reverse = True):
    if(i < 40):
        print "word:", k, "\t","count:", results[k] 
    i = i+1
