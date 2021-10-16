#!/usr/bin/python3
import os
import time
import random as rnd

class Child:
    @staticmethod
    def work(arg: int):
        a = os.getpid()
        print('Child, процесс с PID ', a, 'аргумент', arg)
        time.sleep(arg)
        print('Процесс с PID завершён', a)
        b = rnd.randint(0, 1)
        os._exit(b)


def main():
    Child.work(rnd.randint(5, 10))

main()
