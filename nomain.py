#!/usr/bin/python3
import os
import time
import random

class Child:
    @staticmethod
    def work(arg: int):
        a = os.getpid()
        print('Child, процесс с PID ', a, 'аргумент', arg)
        time.sleep(arg)
        print('Процесс с PID завершён', a)
        b = random.randint(0, 1)
        os._exit(b)


def main():
    Child.work(random.randint(5, 10))

main()
