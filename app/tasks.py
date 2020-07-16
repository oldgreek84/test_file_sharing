import os
import time


def example(sec):
    print('starting task')
    for i in range(sec):
        print(i)
        time.sleep(1)

    print('task complite')
