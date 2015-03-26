import mincemeat
import hashlib


l = []
i = 0;
while i<40000000:
    l.append(i)
    i+=1000000

datasource = dict(enumerate(l))

def mapfn(k,v):
    for j in range(v,v+1000000):
        inputstr = 'fluffy'+`j`
        hash_obj = hashlib.md5(inputstr.encode())
        h = hash_obj.hexdigest()
        if h[:5] == '00000':
            yield inputstr, h
            yield 'matches', 1 

                
def reducefn(k,vals):
    if k=='matches':
        return sum(vals)
    else:
        return vals
    
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

 
for k in results:
    if k != 'matches':
         print k, "->", results[k]
print "matches", ":", results['matches']
