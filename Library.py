import threading
from threading import*
import time
d={}

#creation of key in datastore
def create(key,value,timeout=0):
    if key in d:
        print("error : This key already exists in data ")
    else:
        if(key.isalpha()):
            if((len(d)<1024*1024*1024)and(value<=16*1024*1024)):
                if(timeout==0):
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if(len(key)<=32):
                    d[key]=l
                print("This key is created")
            else:
                print("The size of datastore and value exceeds")
        else:
            print("error: invalid key name")

#reading the key present in datastore
def read(key):
    if key not in d:
        print("error: invalid key")
    else:
        b=d[key]
        if (b[1]==0):
            a=str(key)+":"+str(b[0])
            return a
        else:
            if(time.time()<b[1]):
                a=str(key)+":"+str(b[0])
                return a
            else:
                print("error: Time to live of key has expired")

#deletion of key present in datastore
def delete(key):
    if key not in d:
        print("error: Invalid key")
    else:
        b=d[key]
        if(b[1]==0):
            del d[key]
            print("This key is deleted")
        else:
             if(time.time()<b[1]):
                 del d[key]
                 print("This key is deleted")
             else:
                print("error: Time to live of key has expired")

#modifying key_value in datastore
def modify(key,value):
    if key not in d:
        print("error: Invalid key")
    else:
        b=d[key]
        if(b[1]==0):
            c=[]
            c.append(value)
            c.append(b[1])
            d[key]=c
            print("This key is modified")
        else:
            if(time.time()<b[1]):
                c=[]
                c.append(value)
                c.append(b[1])
                d[key]=c
                print("This key is modified")
            else:
                print("error: Time to live of key has expired")

            
                 


                

                
            
