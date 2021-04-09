# coding=utf-8
# author: Lan_zhijiang
# date: 2021/03/27
# description: run different part files

from tkinter import *

from computer_locker.main import ComputerLocker
from arrangement_system.main import RandomDraw
from log import Log


class ClassroomManagementSystsem:

    def __init__(self):

        self.log = Log()

        self.computer_locker = ComputerLocker(self.log)
        self.random_draw = RandomDraw(self.log)


