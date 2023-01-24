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

def files(path,lamb):
    import os

    global fulllog

    base = 0
    for root, dirs, files in os.walk(path):
        base+=len(files)
    
    total = base
    base = 100/base
    
    bar = "█"
    blank = " "

    i = 0
    last = 0

    for root, dirs, files in os.walk(path):
        for name in files:
            lamb(os.path.realpath(os.path.join(root, name)))
            
            i+=1
            if(base*i-last > 1):
                clear()
                print(fulllog)
                print("|"+bar*int(base*i/3), end="")
                print(blank*(int(base*total/3)-int(base*i/3))+"|")
                
                last = base*i

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
