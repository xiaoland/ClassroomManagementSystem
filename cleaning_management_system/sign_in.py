# coding=utf-8
# author: Lan_zhijiang
# date: 2021/3/28
# description: Sign in process

from base_ai_abilites.face_recognization import FaceReg
from base_device_manager.camera import CameraManager
from base_ai_abilites.tts import BaiduTts

from tkinter import *
import json


class SignIn:

    def __init__(self, log, mode):

        self.log = log
        self.mode = mode

        self.camera_manager = CameraManager(log)
        self.face_reg = FaceReg("file_path", log)
        self.tts = BaiduTts()

        self.names = json.load(open("./data/json/names.json", "r", encoding="utf-8"))

    def run(self):

        """
        启动
        :return:
        """
        self.log.add_log("SignInSystem: running now...", 1)

    def window(self):

        """
        启动UI
        :return:
        """
        window = Tk()
        window.title("签到系统")
        window.geometry('1024x600')

        notice = Label(window, text="请点击按钮拍照签到", font=("Helvetica", 50))
        notice.pack(side=TOP)

        place = Frame(window, height=25, width=50)
        button = Button(place, height=25, width=30, command=self.sign, text="签名")
        button.pack(side=TOP)
        place.pack(side=TOP)

        window.mainloop()

    def sign(self):

        """
        进行签名
        :return:
        """
        img = self.camera_manager.capture_image()
        self.camera_manager.show_image(img)

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

        sign_in_result = json.load(open("./data/json/sign_in_result.json", "r", encoding="utf-8"))
        sign_in_result[self.mode].append(user_id)
        json.dump(sign_in_result, open("./data/json/sign_in_result.json", "w", encoding="utf-8"))
