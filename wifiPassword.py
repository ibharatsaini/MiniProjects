import subprocess

name = input("Enter the name of the WIFI:- ")
path=""

with open(path,"w+") as file:
    p= subprocess.run(['netsh','wlan','show','profile',name,'key=clear'],stdout=file,text=True)

with open(path,"r") as file:
    lines = file.readlines()
    for line in lines:
        if("Key Content" in line.strip()):
            print(line)
