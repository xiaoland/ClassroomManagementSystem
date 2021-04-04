# coding=utf-8
# author: Lan_zhijiang
# date: 2021/03/27
# description: The Main Part of computer locker

from base_ai_abilites.face_recognization import FaceReg
from base_device_manager.camera import CameraManager
# from tkinter import *
# import threading

import json
import schedule
import os
import time


class ComputerLocker:

    def __init__(self, log):

        self.log = log
        self.camera_manager = CameraManager(log)
        self.face_reg = FaceReg("file_path", log)
        # self.root = Tk()
        # self.root.withdraw()

        self.band_list = json.load(open("./data/json/band_to_use_computer_list.json", "r", encoding="utf-8"))

        self.break_timepoint = [
            ("08:30:00", "08:40:00"),
            ("09:20:00", "09:30:00"),
            ("10:10:00", "10:20:00"),
            ("11:00:00", "11:10:00"),
            ("14:50:00", "15:15:00"),
            ("15:55:00", "16:05:00"),
            ("16:45:00", "16:55:00"),
            ("20:30:00", "20:40:00")
        ]

    def run(self):

        """
        启动电脑锁
        :return:
        """
        self.log.add_log("ComputerLocker: run now...", 1)

        # thread_window = threading.Thread(target=self.root.mainloop, args=())
        # thread_window.start()

        for i in range(0, len(self.break_timepoint)):
            self.log.add_log("ComputerLocker: add schedule", 1)
            job = lambda: self.sleep_time_up() # lambda: self.time_up(i)
            schedule.every().day.at(self.break_timepoint[i][0]).do(job)

        while True:
            schedule.run_pending()

    def time_up(self, index):

        """
        到点了，开始检测
        :param index: break_timepoint的第几个
        :return:
        """
        self.log.add_log("ComputerLocker: time is up, index: %s, start checking..." % index, 1)

        self.log.add_log("ComputerLocker: time is up, index: %s, start checking..." % index, 1)

        while True:
            self.camera_manager.capture_image()

            detect_res = self.face_reg.face_detect(self.face_reg.read_img("img.jpg"))
            try:
                face_num = detect_res["result"]["face_num"]
            except KeyError:
                print(detect_res)
                raise KeyError

            if face_num == 0 or face_num is None:
                self.log.add_log("ComputerLocker: Face not detected", 1)
                break
            else:
                self.log.add_log("ComputerLocker: Face detected", 1)

                search_res = self.face_reg.face_search(self.face_reg.read_img("img.jpg"))
                try:
                    user_id = search_res["result"]["user_list"][0]["user_id"]
                    self.log.add_log("ComputerLocker: detect user_id-%s" % user_id, 1)
                except:
                    self.log.add_log("ComputerLocker: error with search result", 1)
                    print(search_res)
                    raise KeyError

                if int(user_id) in self.band_list["inBreak"]:
                    self.log.add_log("ComputerLocker: user_id-%s is in the band_list, going into sleep..." % user_id, 1)
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

                print("end_timepint", self.break_timepoint[index][1])
                if int(self.log.get_formatted_time().replace(":", "")) > int(
                        self.break_timepoint[index][1].replace(":", "")):
                    self.log.add_log("ComputerLocker: break end now", 1)
                    break

            time.sleep(30)

    def sleep_time_up(self):

        time.sleep(90)
        self.log.add_log("ComputerLocker: time is up, fall sleep...", 1)
        os.system("rundll32 powrprof.dll,SetSuspendState")



