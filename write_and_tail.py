#!/usr/bin/env python3
import subprocess
filename = "result.log"

subprocess.Popen(["./write_log.sh"])

# from sh import tail
# runs forever
# for line in tail("-f", "./result.log", _iter=True):
#    print(line, end='')

import time 
import subprocess 
import select 
f = subprocess.Popen(['tail','-F',filename],\
    stdout=subprocess.PIPE,stderr=subprocess.PIPE) 
p = select.poll() 
p.register(f.stdout)
while True:
    time.sleep(3)
    if p.poll(1):
        print (f.stdout.readline())
    else:
        break
