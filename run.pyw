# coding=utf-8
# author: Lan_zhijiang
# date: 2021/03/27
# description: run different part files

from computer_locker import main
from log import Log

log = Log()
computer_locker = main.ComputerLocker(log)

if __name__ == "__main__":
    computer_locker.run()

