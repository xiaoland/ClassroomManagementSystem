# coding=utf-8
# author: Lan_zhijiang
# date: 2021/03/27
# description: run different part files

# from tkinter import *
import threading

from computer_locker.main import ComputerLocker
from arrangement_system.main import RandomDraw
from daily_auto_management_system.main import DailyAutoManagementSystem
from log import Log


class ClassroomManagementSystem:

    def __init__(self):

        self.log = Log()

        self.computer_locker = ComputerLocker(self.log)
        self.random_draw = RandomDraw(self.log)
        self.daily_auto_manager = DailyAutoManagementSystem(self.log)

    def run(self):

        """
        启动
        :return:
        """
        self.log.add_log("ClassroomManagementSystem: run the system", 1)
        locker_thread = threading.Thread(target=self.computer_locker.run)
        daily_auto_thread = threading.Thread(target=self.daily_auto_manager.run)

        locker_thread.start()
        daily_auto_thread.start()


if __name__ == "__main__":
    c = ClassroomManagementSystem()
    c.run()
