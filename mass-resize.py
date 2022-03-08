from os.path import dirname,basename
from PIL import Image

def filename(path):
    import os
    from urllib.parse import urlparse
    
    name = urlparse(path)
    
    return os.path.basename(name.path)

def files(path,lamb=None):
    import os

    fold = os.walk(path)
    ret = []

    once = True

    for root, dirs, files in fold:
        if(once):
            base = (100/len(files))
            bar = "█"
            blank = " "
            i = 0
        for name in files:
            if(lamb != None):
                lamb(os.path.realpath(os.path.join(root, name)))
                if(once):
                    i+=1
                    print("|"+bar*int(base*i/3), end="")
                    print(blank*(int(base*len(files)/3)-int(base*i/3))+"|")
            
            ret.append(os.path.realpath(os.path.join(root, name)))
        
        once = False
     
    return ret

def resize(f):
    scale = lambda x,y: (int((x[0]/100)*y),int((x[1]/100)*y))
    
    try:
        img = Image.open(f)
        img = img.resize(scale(img.size,50))
        img.save(f)

        print(f+": ok")
    except:
        print("error on file :"+f)

def run():
    from os.path import exists, realpath
    from os import mkdir, chdir
    from shutil import rmtree as rmdir
    from shutil import copytree as copy
    
    if(exists("output")):
        rmdir("output")

    print("making a copy...")
    copy("f:/img","output")
    
    print(realpath("output"))

    print("starting...")
    files("output", resize)

run()
