from os.path import dirname,basename
from PIL import Image

def clear():
    from os import system
    import os

    system("cls" if os.name=="nt" else "clear")

def filename(path):
    import os
    from urllib.parse import urlparse
    
    name = urlparse(path)
    
    return os.path.basename(name.path)

def files(path,lamb=None):
    import os

    global fulllog
    
    fold = os.walk(path)
    ret = []

    once = True

    for root, dirs, files in fold:
        if(once):
            base = (100/len(files))
            
            bar = "█"
            blank = " "

            i = 0
            last = 0

        for name in files:
            if(lamb != None):
                lamb(os.path.realpath(os.path.join(root, name)))
                if(once):
                    i+=1
                    if(base*i-last > 5):
                        clear()
                        print(fulllog)
                        print("|"+bar*int(base*i/3), end="")
                        print(blank*(int(base*len(files)/3)-int(base*i/3))+"|")
                        
                        last = base*i
            
            ret.append(os.path.realpath(os.path.join(root, name)))
        
        once = False
     
    return ret

def resize(f,percent):
    global fulllog

    scale = lambda x,y: (int((x[0]/100)*y),int((x[1]/100)*y))
    
    try:
        img = Image.open(f)
        img = img.resize(scale(img.size,percent))
        img.save(f)

        fulllog+=log(f+": ok")
    except:
        fulllog+=log("error on file :"+f)

def log(text):
    text = text.upper()
    print(text)

    return text+"\n"

fulllog = ""

def run():
    from os.path import exists, realpath
    from os import mkdir, chdir
    from shutil import rmtree as rmdir
    from shutil import copytree as copy
    import argparse

    global fulllog
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("path")
    parser.add_argument("percent")
    
    args = parser.parse_args()
    
    if(exists("output")):
        fulllog+=log("removing output...")
        rmdir("output")

    fulllog+=log("making a copy...")
    
    copy(args.path,"output")
    
    fulllog+= log("rescaled images will be in :"+realpath("output")+".") 

    fulllog+=log("starting...\n")
    
    callback = lambda file,percent=int(args.percent.replace("%","")): resize(file,percent)

    files("output", callback)

run()
