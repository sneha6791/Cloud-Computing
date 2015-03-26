# Client Side Coding in python for the CHAT ROOM!

import rpyc
from threading import Thread

ctr=0
def myprint(message): # Function to print out the chats
  print message

def client_broadcast(): # Function to broadcast to other clients
  while 1:
    global ctr
    length = conn.root.msglength()
    if ctr < length:
      msg = conn.root.broadcast(ctr)# has to appear on other client screens
      print msg
      ctr = ctr + 1

conn = rpyc.connect("localhost",18888)
name = raw_input("Enter your name: ")
print "Type 'bye' to exit chat room!"
conn.root.setCallback(myprint, name)
conn.root.notify(name)
ctr = conn.root.msglength()

t2=Thread(target = client_broadcast)
t2.daemon=True
t2.start()
while 1:
  message = raw_input()
  if message == "bye":   #Final exit statement check
    conn.root.notify_exit(name)
    #t2.stop()		
    break	
  conn.root.serverPrint(message,name)
  ctr = ctr+1
   
conn.close()  # Close Server connection
