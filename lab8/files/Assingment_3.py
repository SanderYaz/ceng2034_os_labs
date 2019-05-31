import os
import json
import shutil, random
#Data.json has file extension magic numbers
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")) as data_file:
    data = json.loads(data_file.read())
#Info file
class Info:
    def __init__(self, type_, extension, mime):
        self.type = type_
        self.extension = extension
        self.mime = mime
#Detect file
def get(obj):
    if not isinstance(obj, bytes):
        raise TypeError("object type must be bytes")
    info = {
        "type": dict(),
        "extension": dict(),
        "mime": dict()  }
    stream = " ".join(['{:02X}'.format(byte) for byte in obj])
    for element in data:
        for signature in element["signature"]:
            offset = element["offset"] * 2 + element["offset"]
            if signature == stream[offset:len(signature) + offset]:
                for key in ["type", "extension", "mime"]:
                    info[key][element[key]] = len(signature)
                    
    for key in ["type", "extension", "mime"]:
        info[key] = [element for element in sorted(info[key], key=info[key].get, reverse=True)]
    return Info(info["type"], info["extension"], info["mime"])

#for i in range (10,150):
    #name = "{0}{1}".format("file", i)
    #origin = "{0}{1}".format("file", random.randint(1,4))
    #shutil.copyfile(origin, name)

sander = list()
current_directory_2 = os.getcwd()
for file in os.listdir(current_directory_2):
    with open(file, "rb") as file2:
    	sy = get(file2.read(128))
    if (sy.extension == []):
        sander.append("['ASCI txt']")
    else:
        sander.append(sy.extension)
    if (sy.extension == []):
        print(file, "['ASCI txt']")
    else:
        print(file, sy.extension)

def unique(list1): 
    unique_list = [] 
    for x in list1: 
        if x not in unique_list: 
            unique_list.append(x) 
    print ("There are",len(unique_list),"types of files in files directory")
unique(sander)