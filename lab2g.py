#!/usr/bin/env python3

#Author: Manik Shrestha
#Author ID: 162458210
#Date Created: 2025/01/23

import sys



if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])
    
while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')
