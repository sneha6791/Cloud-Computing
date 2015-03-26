import mincemeat
import sys
import math
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
    if count % length == 0:
        input_list.append((old_line+line).replace('\n',' '))
        old_line = ''
    else:
        old_line= old_line+line
    count+=1



datasource = dict(enumerate(input_list))


def mapfn(k,v):
    i = 0
    while i+333<=10000:
        for n in v.split():
            if int(n) in range(i,i+333):
                yield i+332, 1
            else:
                yield i+332, 0
            if(i==0):
                yield 'totalcount',1
        i+=333
       
           
        
def reducefn(k,vals):
    return sum(vals)
    
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")


print "Range","\t\t","%"
for k in sorted(results.iterkeys()):
    if k!= 'totalcount':
        l = int(k) - 332
        print l, "-", k,"\t", (float(results[k]) / results['totalcount'])*100,"%","\t"," ",
        for j in range(0,results[k]):
            sys.stdout.write("*")
    print "\n"
