# coding=utf-8
# author: Lan_zhijiang
# date: 2021/04/09
# description: The Main Part of daily auto management system

import schedule
import json
from base_ai_abilites.tts import BaiduTts


class DailyAutoManagementSystem:

    def __init__(self, log):

        self.log = log
        self.tts = BaiduTts()

        self.daily_schedule = json.load(open("./data/json/daily_schedule.json", "r", encoding="utf-8"))

    def run(self):

        """
        启动
        :return:
        """
        self.log.add_log("DailyAutoManagementSystem: start", 1)

        for i in range(0, len(self.daily_schedule["onClassTime"]["morning"])):
            self.log.add_log("DailyAutoManagementSystem: add morning schedule", 1)
            schedule.every().day.at(self.daily_schedule["onClassTime"]["morning"][i][0]).do(lambda: self.time_up("morning", "class_on", i))
            schedule.every().day.at(self.daily_schedule["onClassTime"]["morning"][i][1]).do(lambda: self.time_up("afternoon", "class_off", i))

        for i in range(0, len(self.daily_schedule["onClassTime"]["afternoon"])):
            self.log.add_log("DailyAutoManagementSystem: add afternoon schedule", 1)
            schedule.every().day.at(self.daily_schedule["onClassTime"]["afternoon"][i][0]).do(lambda: self.time_up("afternoon", "class_on", i))
            schedule.every().day.at(self.daily_schedule["onClassTime"]["afternoon"][i][1]).do(lambda: self.time_up("afternoon", "class_off", i))

    def time_up(self, time_part, point_type, index):

        """
        时间点到达
        :return:
        """
        self.log.add_log("DailyAutoManagementSystem: p_t: %s, index: %s is up" % (point_type, index), 1)

        if time_part == "afternoon":
            index+=

        if point_type == "class_on" and index != 0:
            class_name = self.daily_schedule["classArrangement"][self.log.get_weekday()][index]
            if class_name == "历史":
                self.tts.start("哦吼吼吼！这不是范老师吗，欢迎欢迎！——同学们，——起立！")
        elif point_type == "class_off":
            pass



