import mincemeat
import sys
import math

f = open(sys.argv[1],'r')
data = list(f)
length = len(data)
f.close()
input_list = []
count = 1
old_line = ''
for line in file(sys.argv[1]):
    if count % length == 0:
        input_list.append((old_line+line).replace('\n',' '))
        old_line = ''
    else:
        old_line= old_line+line
    count+=1



datasource = dict(enumerate(input_list))


def mapfn(k,v):
    for n in v.split():
        yield 'totalcount', 1
        yield 'sum',int(n)
        yield 'ssum',int(n)*int(n)
        
def reducefn(k,vals):
    return sum(vals)
    
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print "sum", results['sum']
print 'total count', results['totalcount']
avg = float(results['sum'])/results['totalcount']
var = (float(results['ssum'])/results['totalcount'])-(avg)**2
print 'stddev', math.sqrt(var)
