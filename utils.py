import random
import string
import os
import shutil
import time
import datetime

def getCsvFilesFromDirectory(path):
    csvFiles = []
    for file in os.listdir(path):
        if file.endswith(".CSV"):
            csvFiles.append(os.path.join(path, file))
    
    return csvFiles

def getCurrentTimestamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st

def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def createFolder(path):
    try:  
        os.mkdir(path)
    except OSError:  
        print ("Creation of the directory %s failed" % path)
    else:  
        print ("Successfully created the directory %s " % path)

def deleteFolder(path):
    try:
        shutil.rmtree(path)
    except shutil.Error as e:
        print ("Deletion of the directory %s failed: %s" % (path, e))
    else:
        print ("Successfully deleted the directory %s " % path)

def deleteFile(path):
    try:
        os.remove(path)
    except OSError:
        print ("Removeal of the file %s failed" % path)
    else:  
        print ("Successfully removed the file %s " % path)

if __name__ == '__main__':
    print(randomStringDigits(10))
    createFolder('./bobby')
    print('hello')
    deleteFolder('./bobby')
    