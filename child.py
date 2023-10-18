#! /usr/bin/python3

import os
import time
import sys
import random

print("child:[{0}]: I am started. My PID {0}. Parent PID {1}".format(os.getpid(), os.getppid()))
time.sleep(int(sys.argv[1]))
print("Child[{0}]: I am ended. PID {0}. Parent PID {1}".format(os.getpid(), os.getppid()))
exit(random.randint(0, 1))