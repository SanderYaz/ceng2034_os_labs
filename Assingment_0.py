import os, os.path, time

#change working directory to new created folder.
os.chdir('/home')
os.system('mkdir -p $HOME/os_lab_0')
os.chdir(os.path.expanduser('~')+"/os_lab_0")

#create new 2 .txt file and 1 .py file in the folder.

file = open("sander1.txt", "w") 
file = open("sander2.txt", "w") 
file = open("sander3.py", "w") 
file.write("SANDER Yazıcıoglu") 
file.close() 

#print all files last modified date in the folder.

current_directory = os.getcwd()
for file in os.listdir(current_directory):
	print("---"+file+"---")
	print("last modified: %s" % time.ctime(os.path.getmtime(file)))
	print("created: %s" % time.ctime(os.path.getctime(file)))


#find only txt files in the folder.

current_directory_2 = os.getcwd()
for file in os.listdir(current_directory_2):
    if file.endswith(".txt"):
        print(os.path.join(current_directory_2, file))

#160709028 Sander YAZICIOGLU


