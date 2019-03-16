#!/usr/bin/python
import os,sys

#Create jail path
os.system('mkdir /chroot')
os.system('mkdir /chroot/bin')
os.chdir ('/chroot')
chroot ="/chroot"
os.system('mkdir bin dev etc home  home/prisoner lib lib64 var usr usr/bin')

#copy bash file
os.system ('sudo cp /bin/bash /chroot/bin/')
os.system ('sudo cp /lib64/ld-linux-x86-64.so.2 /chroot/lib/x86_64-linux-gnu')
os.system ('sudo cp /lib/x86_64-linux-gnu/libtinfo.so.5 /chroot/lib/x86_64-linux-gnu')
os.system ('sudo cp /lib/x86_64-linux-gnu/libdl.so.2 /chroot/lib/x86_64-linux-gnu')
os.system ('sudo cp /lib/x86_64-linux-gnu/libc.so.6 /chroot/lib/x86_64-linux-gnu')

#copy python3 file
os.system ('sudo cp /usr/bin/python3 /chroot/usr/bin/python3')
os.system ('sudo cp /lib64/ld-linux-x86-64.so.2 /chroot/lib/x86_64-linux-gnu')
os.system ('sudo cp /lib/x86_64-linux-gnu/libpthread.so.0 /chroot/lib/x86_64-linux-gnu')
os.system ('sudo cp /lib/x86_64-linux-gnu/libc.so.6 /chroot/lib/x86_64-linux-gnu')
os.system ('sudo cp /lib/x86_64-linux-gnu/libdl.so.2 /chroot/lib/x86_64-linux-gnu')
os.system ('sudo cp /lib/x86_64-linux-gnu/libutil.so.1 /chroot/lib/x86_64-linux-gnu')
os.system ('sudo cp /lib/x86_64-linux-gnu/libexpat.so.1 /chroot/lib/x86_64-linux-gnu')
os.system ('sudo cp /lib/x86_64-linux-gnu/libz.so.1 /chroot/lib/x86_64-linux-gnu')
os.system ('sudo cp /lib/x86_64-linux-gnu/libm.so.6 /chroot/lib/x86_64-linux-gnu')
os.chdir (chroot)
file = open("sander.py", "w") 
file.write("print ('Hello World')") 
file.close()
os.chroot(chroot)
#os.system ('sudo chroot /chroot /bin/bash')
print(os.getcwd()) #Check chroot
os.chroot(python3 /sander.py) #Doesn't Work

