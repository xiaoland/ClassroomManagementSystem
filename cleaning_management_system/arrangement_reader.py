# coding=utf-8
# author: Lan_zhijiang
# date: 2020/12/6
# description: read in arrangement

import json


class ArrangementReader:

    def __init__(self, log):

        self.log = log
        self.names = json.load(open("./data/json/names.json", "r", encoding="utf-8"))
        self.raw_arrangement = {}
        self.class_arrangement = {}
        self.public_labor_arranagement = []

    def read_in(self):

        """
        读入安排表
        :return:
        """
        self.log.add_log("Reader: reading arrangement...", 1)
        self.raw_arrangement = json.load(open("./data/json/labor_arrangement.json", "r", encoding="utf-8"))
        self.class_arrangement = self.raw_arrangement["教室"]
        self.public_labor_arranagement = self.raw_arrangement["工地"]

    def get_pubilc_labor_arrangement(self):

        """
        返回工地人员名单(str)
        :return: str
        """
        return self.get_names(self.public_labor_arranagement)

    def get_names(self, lists):

        """
        :param lists: 列表
        :return:
        """
        names = ""
        for name in lists:
            names = names + name + "你负责第" + str(lists.index(name) + 1) + "列，"
        return names

    def get_name(self, user_id):

        """
        获取名字
        :param user_id:
        :return:
        """
        return self.names[str(user_id)]["name"]

    def get_index(self, name, lists):

        """

        :param name:
        :param lists:
        :return:
        """
        try:
            index = lists.index(name)
            print("INDEX: ", index)
        except ValueError:
            return False
        else:
            return index
