#! /usr/bin/python3
import sys
import os
import time
import random


def child(sleep_time):
    print("child[{0}]: I am started. My PID {0}. Parent PID {1}.".format(os.getpid(), os.getppid()))
    time.sleep(sleep_time)
    print("Child[{0}]: I am ended. PID {0}. Parent PID {1}".format(os.getpid(), os.getppid()))
    code = random.randint(0, 1)
    exit(code)


if len(sys.argv) < 2:
    print("Set the children number")
    exit(1)
count = int(sys.argv[1])
parent_pid = os.getpid()

for i in range(count):
    status = os.fork()
    if status > 0:
        print("Parent[{0}]: I run children process with PID {1}".format(parent_pid, status))
    elif status == 0:
        env = ["./child", str(random.randint(5, 10))]
        os.execve("./child", env, os.environ)

children = count
while children > 0:
    status = os.wait()
    print("Parent[{0}]: Child with PID {1} terminated. Exit Status {2}.".format(parent_pid, status[0], status[1]))
    if status[1] == 0:
        children -= 1
    else:
        new_child_status = os.fork()
        if new_child_status == 0:
            env = ["./child", str(random.randint(5, 10))]
            os.execve("./child", env, os.environ)
