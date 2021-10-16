#!/usr/bin/python3
import os
import random as rnd
import time


# author: Тыщенко Леонид, 11-902

class Parent:
    @staticmethod
    def work(fork_count: int):
        a = []
        for i in range(1, fork_count):
            b = os.fork()
            if b == 0:
                c = rnd.randint(5, 10)
                os.execl("child.py", str(c))
            else:
                a.append(b)
        while a:
            b, exit_code = os.wait()
            if b == 0:
                c = rnd.randint(1, 10)
                time.sleep(c)
            else:
                print("Дочерний процесс с PID", b, "завершён. Статус завершения.", exit_code)
                a.remove(b)


def main():
    Parent.work(int(input()))


main()