# coding=utf-8
# author: Lan_zhijiang
# date: 2020/09/01
# description: 根据班级json文件进行随机摇号

import random
import json


class RandomDraw:

    def __init__(self, log):

        self.log = log

        self.number_limit = 55
        self.reset = False
        self.data_json_fp = "./data/json/class_9_id_list.json"
        self.pass_json_fp = "./data/json/ramdom_pass_index_list.json"

        self.data = {}
        self.data_keys = []
        self.pass_data = []

        self.result = []

    def main(self):

        """
        主程序
        :return:
        """
        for i in range(0, self.number_limit):
            random_index = random.randint(1, len(self.data_keys))
            if random_index in self.pass_data:
                print("pass: ", random_index)
                continue
            else:
                self.pass_data.append(random_index)
                name = self.data[str(random_index)]["name"]
                self.result.append(name)
                print(name)

    def init(self):

        """
        初始化数据
        :return:
        """
        self.data = json.load(open(self.data_json_fp, "r", encoding="utf-8"))
        self.data_keys = list(self.data.keys())
        if self.reset:
            pass
        else:
            self.pass_data = json.load(open(self.pass_json_fp, "r", encoding="utf-8"))

    def run(self):

        """
        启动
        :return:
        """
        self.log.add_log("RandomDraw: run now, n_l: %s" % self.number_limit, 1)
        self.init()
        self.main()

        if self.reset:
            self.log.add_log("RandomDraw: saving the pass_data")
            json.dump(self.pass_data, open(self.pass_json_fp, "w", encoding="utf-8"))

        return self.result


# random_pick()
# json.dump(pass_data, open(pass_json_fp, "w", encoding="utf-8"))
