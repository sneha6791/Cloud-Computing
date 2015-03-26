# Server Side Coding for CHAT ROOM!

import rpyc
import time
from sets import Set

class MyService(rpyc.Service):
        
    def on_connect(self): # Like a Constructor
        self.fn = None

    def exposed_msglength(self):  # Returns the length of the msg_list
        return len(msg_list)

    def exposed_notify(self,name):  # Function to notify the user entry to the chat room
	msg = name +" has entered the chat room."
	for a in client_list:
		if a is not self.fn:
			a(msg)

    def exposed_notify_exit(self,name): # Function to notify the user exit from the chat room
        client_list.remove(self.fn)
        msg = name + " has left the chat room."
        for a in client_list:
		if a is not self.fn:
		 	a(msg)

    def exposed_broadcast(self,ctr):  # Returns the requested message
        return msg_list[ctr]

    def exposed_serverPrint(self,message,n):  #Appends message to the msg_list
	msg = n + " : " + message
        msg_list.append(msg)
       
    def exposed_setCallback(self,fn,n):  # Adds client reference to a list
        self.fn = fn
        client_list.add(self.fn)
        
if __name__ == "__main__":
    msg_list = [] # List to append all the messages received
    client_list = Set([]) # Removes duplicates
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port = 18888)
    t.start()
