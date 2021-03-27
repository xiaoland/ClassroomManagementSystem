# coding=utf-8
# author: Lan_zhijiang
# date: 2020/12/6
# description: The Main Part

from log import Log
from base_ai_abilites.face_recognization import FaceReg
from cleaning_management_system.arrangement_reader import ArrangementReader
from base_device_manager.camera import CameraManager
from base_ai_abilites.tts import BaiduTts
import threading
from tkinter import *
import time
import json


class Init:

    def __init__(self):

        self.log = Log()
        self.face_reg = FaceReg("file_path", self.log)
        self.arrangement_reader = ArrangementReader(self.log)
        self.camera_manager = CameraManager(self.log)
        self.tts = BaiduTts()

        self.is_end = False

        self.sign_result = {
            "扫地": {},
            "拖地": {},
            "柜台+工具处": {},
            "摆桌椅": {},
            "窗户+窗台": {},
            "黑板+讲台": {},
            "倒垃圾": {},
            "走廊": {}
        }

    def time_count(self, second, callback):

        """
        计时器
        :param second: 计算的秒数
        :param callback: 时间到以后的callback
        :return:
        """
        self.log.add_log("Init: Start time count for" + str(second), 1)
        time.sleep(second)
        callback()

    def generate_report(self):

        """
        开始生成报告
        :return:
        """
        json.dump(self.sign_result, open("./data/json/report.json", "w", encoding="utf-8"))

    def init_sign_window(self):

        """
        初始化签名窗口
        :return:
        """

        # INIT THE SIGN WINDOW
        window = Tk()
        window.title("自动劳动签到系统")
        window.geometry('1024x600')

        # SET THE NOTICE LABLE
        notice = Label(window, text="请点击按钮并签到", font=("Helvetica", 20))
        notice.pack(side=TOP)

        # 摆桌椅Frame
        desk_place = Frame(window, height=25)
        desc_desk = Label(desk_place, text="摆桌椅签名区", font=("Helvetica", 15))
        desc_desk.pack(side=TOP)
        row_1_button = Button(desk_place, height=10, width=10, command=lambda : self.sign(1, 1), text="列1")
        row_1_button.pack(side=LEFT)
        row_2_button = Button(desk_place, height=10, width=10, command=lambda: self.sign(1, 2), text="列2")
        row_2_button.pack(side=LEFT)
        row_3_button = Button(desk_place, height=10, width=10, command=lambda: self.sign(1, 3), text="列3")
        row_3_button.pack(side=LEFT)
        row_4_button = Button(desk_place, height=10, width=10, command=lambda: self.sign(1, 4), text="列4")
        row_4_button.pack(side=LEFT)
        row_5_button = Button(desk_place, height=10, width=10, command=lambda: self.sign(1, 5), text="列5")
        row_5_button.pack(side=LEFT)
        row_6_button = Button(desk_place, height=10, width=10, command=lambda: self.sign(1, 6), text="列6")
        row_6_button.pack(side=LEFT)
        row_7_button = Button(desk_place, height=10, width=10, command=lambda: self.sign(1, 7), text="列7")
        row_7_button.pack(side=LEFT)
        row_8_button = Button(desk_place, height=10, width=10, command=lambda: self.sign(1, 8), text="列8")
        row_8_button.pack(side=LEFT)

        desk_place.pack(side=TOP)

        # 窗户+窗台签名区
        window_place = Frame(window, height=25)
        window_desk = Label(window_place, text="窗户+窗台签名区", font=("Helvetica", 15))
        window_desk.pack(side=TOP)
        row_1_button = Button(window_place, height=10, width=10, command=lambda: self.sign(2, 1), text="窗1")
        row_1_button.pack(side=LEFT)
        row_2_button = Button(window_place, height=10, width=10, command=lambda: self.sign(2, 2), text="窗2")
        row_2_button.pack(side=LEFT)
        row_3_button = Button(window_place, height=10, width=10, command=lambda: self.sign(2, 3), text="窗3")
        row_3_button.pack(side=LEFT)
        row_4_button = Button(window_place, height=10, width=10, command=lambda: self.sign(2, 4), text="窗4")
        row_4_button.pack(side=LEFT)

        window_place.pack(side=TOP)

        # 黑板签名区
        bb_place = Frame(window, height=25, width=50)
        bb_notice = Label(bb_place, text="黑板+图书角签名区", font=("Helvetica", 15))
        bb_notice.pack(side=TOP)
        button = Button(bb_place, height=10, width=10, command=lambda: self.sign(3, 1), text="点ME")
        button.pack(side=LEFT)

        # ATTENTION: PACK IN THE END

        # 扫地签名
        sweep_place = Frame(window, height=25)
        sweep_notice = Label(sweep_place, text="扫地签名区", font=("Helvetica", 15))
        sweep_notice.pack(side=TOP)
        row_1_button = Button(sweep_place, height=10, width=10, command=lambda: self.sign(4, 1), text="列1")
        row_1_button.pack(side=LEFT)
        row_2_button = Button(sweep_place, height=10, width=10, command=lambda: self.sign(4, 2), text="列2")
        row_2_button.pack(side=LEFT)
        row_3_button = Button(sweep_place, height=10, width=10, command=lambda: self.sign(4, 3), text="列3")
        row_3_button.pack(side=LEFT)
        row_4_button = Button(sweep_place, height=10, width=10, command=lambda: self.sign(4, 4), text="列4")
        row_4_button.pack(side=LEFT)
        row_5_button = Button(sweep_place, height=10, width=10, command=lambda: self.sign(4, 5), text="列5")
        row_5_button.pack(side=LEFT)
        row_6_button = Button(sweep_place, height=10, width=10, command=lambda: self.sign(4, 6), text="列6")
        row_6_button.pack(side=LEFT)
        row_7_button = Button(sweep_place, height=10, width=10, command=lambda: self.sign(4, 7), text="列7")
        row_7_button.pack(side=LEFT)
        row_8_button = Button(sweep_place, height=10, width=10, command=lambda: self.sign(4, 8), text="列8")
        row_8_button.pack(side=LEFT)
        row_9_button = Button(sweep_place, height=10, width=10, command=lambda: self.sign(4, 9), text="后面+讲台")
        row_9_button.pack(side=LEFT)

        sweep_place.pack(side=TOP)

        # 拖地签名
        mop_place = Frame(window, height=25)
        mop_notice = Label(window, text="拖地签名区", font=("Helvetica", 15))
        mop_notice.pack(side=TOP)
        row_1_button = Button(mop_place, height=10, width=10, command=lambda: self.sign(5, 1), text="列1")
        row_1_button.pack(side=LEFT)
        row_2_button = Button(mop_place, height=10, width=10, command=lambda: self.sign(5, 2), text="列2")
        row_2_button.pack(side=LEFT)
        row_3_button = Button(mop_place, height=10, width=10, command=lambda: self.sign(5, 3), text="列3")
        row_3_button.pack(side=LEFT)
        row_4_button = Button(mop_place, height=10, width=10, command=lambda: self.sign(5, 4), text="列4")
        row_4_button.pack(side=LEFT)
        row_5_button = Button(mop_place, height=10, width=10, command=lambda: self.sign(5, 5), text="列5")
        row_5_button.pack(side=LEFT)
        row_6_button = Button(mop_place, height=10, width=10, command=lambda: self.sign(5, 6), text="列6")
        row_6_button.pack(side=LEFT)
        row_7_button = Button(mop_place, height=10, width=10, command=lambda: self.sign(5, 7), text="列7")
        row_7_button.pack(side=LEFT)
        row_8_button = Button(mop_place, height=10, width=10, command=lambda: self.sign(5, 8), text="列8")
        row_8_button.pack(side=LEFT)
        row_8_button = Button(mop_place, height=10, width=10, command=lambda: self.sign(5, 9), text="后面+讲台")
        row_8_button.pack(side=LEFT)

        mop_place.pack(side=TOP)

        # 倒垃圾签名
        trash_place = Frame(window, height=25, width=50)
        trash_notice = Label(trash_place, text="倒垃圾签名区", font=("Helvetica", 15))
        trash_notice.pack(side=TOP)
        button = Button(trash_place, height=10, width=10, command=lambda: self.sign(6, 1), text="点ME")
        button.pack(side=LEFT)

        trash_place.pack(side=LEFT)

        # 杂物间签名区
        room_place = Frame(window, height=25, width=50)
        room_notice = Label(room_place, text="杂物间签名区", font=("Helvetica", 15))
        room_notice.pack(side=TOP)
        button = Button(room_place, height=10, width=10, command=lambda: self.sign(7, 1), text="点ME")
        button.pack(side=LEFT)

        room_place.pack(side=LEFT)

        bb_place.pack(side=LEFT)

        # RUN THE WINDOW
        window.mainloop()

    def sign(self, command, row):

        """
        进行签名
        :param command: 签到模式
        :param row: 列数
        :return:
        """
        img = self.camera_manager.capture_image()
        self.camera_manager.show_image(img)

        self.generate_report()
        detect_res = self.face_reg.face_detect(self.face_reg.read_img("img.jpg"))
        try:
            face_num = detect_res["result"]["face_num"]
        except KeyError:
            print(detect_res)
            raise KeyError

        while True:
            if face_num == 0:
                self.tts.start("没有检测到人脸，请对准摄像头重拍")
            else:
                # self.tts.start("Face Detected. Start searching...")
                break

        search_res = self.face_reg.face_search(self.face_reg.read_img("img.jpg"))
        try:
            user_id = search_res["result"]["user_list"][0]["user_id"]
        except:
            print(search_res)
            raise KeyError

        if command == 1:
            index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                      self.arrangement_reader.class_arrangement["摆桌椅"])
            if index is False:
                self.tts.start("你可不是干这个的啊！")
                return
            if index + 1 == int(row):
                self.sign_result["摆桌椅"][index] = True
                self.tts.start("签到完成")

                next_name = self.arrangement_reader.class_arrangement["扫地"][index]
                self.tts.start("请" + next_name + "同学开始扫地")
                self.tts.start("你负责的是" + str(index + 1) + "列，要扫干净哦！第九列是指教室的后面和讲台")

            else:
                self.tts.start("错误的人脸和对应列数！")
        elif command == 2:
            index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                      self.arrangement_reader.class_arrangement["窗户+窗台"])
            if index is False:
                self.tts.start("你可不是干这个的啊！")
                return

            if index + 1 == int(row):
                self.sign_result["窗户+窗台"][index] = True
                self.tts.start("签到完成")
            else:
                self.tts.start("错误的人脸和对应窗户号！")
        elif command == 3:
            index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                      self.arrangement_reader.class_arrangement["图书角+黑板+讲台"])
            if index is False:
                self.tts.start("你可不是干这个的啊！")
                return

            self.sign_result["图书角+黑板+讲台"][index] = True
            self.tts.start("签到完成")
        elif command == 4:
            index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                      self.arrangement_reader.class_arrangement["扫地"])
            if index is False:
                self.tts.start("你可不是干这个的啊！")
                return

            if index + 1 == int(row):
                try:
                    if self.sign_result["摆桌椅"][index] is True:

                        self.sign_result["扫地"][index] = True
                        self.tts.start("签到完成")

                        next_name = self.arrangement_reader.class_arrangement["拖地"][index]
                        self.tts.start("请" + next_name + "同学开始拖地")
                        self.tts.start("你负责的是" + str(index + 1) + "列，要拖干净哦！第九列是指教室的后面和讲台")

                        is_end = True
                        for i in self.sign_result["扫地"].keys():
                            if self.sign_result["扫地"][i] is False:
                                is_end = False
                        if is_end:
                            trash = self.arrangement_reader.get_names(self.arrangement_reader.class_arrangement["倒垃圾"])

                            self.tts.start(trash)
                            self.tts.start("请这些同学现在开始倒垃圾")
                except KeyError:
                    self.tts.start("摆桌椅的还没摆完呢！")
                    return
                else:
                    self.tts.start("你的任务还没有开始呢！")
                    # c = str(input("ALLOW?: "))
                    # if c == 1:
                    #     self.sign_result["扫地"][index] = True
                    #     self.tts.start("签到完成")
            else:
                self.tts.start("错误的人脸和对应列数！")
        elif command == 5:
            index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                      self.arrangement_reader.class_arrangement["拖地"])
            if index is False:
                self.tts.start("你可不是干这个的啊！")
                return

            if index + 1 == int(row):
                try:
                    if self.sign_result["扫地"][index] is True:
                        self.sign_result["拖地"][index] = True
                        self.tts.start("签到完成")

                        is_end = True
                        for i in self.sign_result["拖地"].keys():
                            if self.sign_result["拖地"][i] is False:
                                is_end = False
                        if is_end:
                            room = self.arrangement_reader.get_names(self.arrangement_reader.class_arrangement["杂物间+柜台"])

                            self.tts.start(room)
                            self.tts.start("这些同学则现在开始清理杂物间和柜台")
                    else:
                        self.tts.start("你的任务还没有开始呢！")
                        # c = str(input("ALLOW?: "))
                        # if c == 1:
                        #     self.sign_result["拖地"][index] = True
                        #     self.tts.start("签到完成")
                except KeyError:
                    self.tts.start("扫地的还没扫呢！你怎么签名")
                    # c = str(input("ALLOW?: "))
                    # if c == 1:
                    #     self.sign_result["拖地"][index] = True
                    #     self.tts.start("签到完成")
                    return
            else:
                self.tts.start("错误的人脸和对应列数！")
        elif command == 6:
            index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                      self.arrangement_reader.class_arrangement["倒垃圾"])
            if index is False:
                self.tts.start("你可不是干这个的啊！")
                return

            self.sign_result["倒垃圾"][index] = True
            self.tts.start("签到完成")
        elif command == 7:
            index = self.arrangement_reader.get_index(self.arrangement_reader.get_name(int(user_id)),
                                                      self.arrangement_reader.class_arrangement["杂物间+柜台"])

            if index is False:
                self.tts.start("你可不是干这个的啊！")
                return
            self.sign_result["杂物间+柜台"][index] = True
            self.tts.start("签到完成")

    def phase1_start(self):

        """
        run
        :return:
        """
        self.log.add_log("Phase1: now start", 1)
        self.tts.start("现在，开始第一阶段。请以下同学留下，其余同学全部出去或在后面等着")
        table = self.arrangement_reader.get_names(self.arrangement_reader.class_arrangement["摆桌椅"])
        window = self.arrangement_reader.get_names(self.arrangement_reader.class_arrangement["窗户+窗台"])
        blackboard = self.arrangement_reader.get_names(self.arrangement_reader.class_arrangement["图书角+黑板+讲台"])

        self.tts.start(table)
        self.tts.start("这些同学负责摆桌椅，现在开始工作。按照摆完以后请过来选择列数完成签名，")
        self.tts.start("摆桌椅要求：全部拉开，保 证一定距离以方面扫地拖地；椅子要翻上去")

        time.sleep(0.5)
        self.tts.start(window)
        self.tts.start("然后，这些同学负责擦窗台和窗户。按照读的顺序，每人一个窗，从只有窗户的一侧从前往后数，门的一侧也是从前往后数")
        self.tts.start("窗户要求：用抹布擦干以后找报纸弄干，擦的时候要有规律，水不要太多。没有抹布要么等要么去对面借，完成以后过来签名")

        time.sleep(0.5)
        self.tts.start(blackboard)
        self.tts.start("这些同学负责整理黑板、图书柜、讲台")
        self.tts.start("黑板要擦干净，擦完以后一定打开屏幕，不要遮住了。讲台不要有垃圾，粉笔灰擦干净，完成后过来签名")

        video_recorder = threading.Thread(target=self.camera_manager.capture_video, args=("phase1-record1.mp4",))
        video_recorder.start()

        self.init_sign_window()

    def run(self):

        """
        启动程序
        :return:
        """
        self.log.add_log("Init: System is now running...", 1)
        self.log.add_log("Init: Initializing...", 1)
        time_count_thread = threading.Thread(target=self.time_count, args=(1200, self.generate_report))
        time_count_thread.start()

        self.tts.start("Hi~ 这里是YYH开发的【自动劳动管理系统】")
        self.tts.start("主人~ 现在，是时候开始劳动了~")
        #
        self.arrangement_reader.read_in()

        # public = self.arrangement_reader.get_names(self.arrangement_reader.public_labor_arranagement)
        # self.tts.start(public)
        # self.tts.start("这些同学马上跟着正诺恒，拿上一个扫把和垃圾铲，还有两个垃圾袋去工地！")

        self.phase1_start()

        self.generate_report()


if __name__ == "__main__":
    classes = Init()
    classes.run()


