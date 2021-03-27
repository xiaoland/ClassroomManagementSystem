# coding=utf-8
# author: Lan_zhijiang
# date: 2020/12/5
# description: baidu tts

import requests
from urllib import request, parse
from base_device_manager.player import Player


class BaiduTts:

    def __init__(self):

        self.player = Player()

        self.token = ""
        self.app_id = "TSFp0BKH547h7Agjf2WkV2Ll"
        self.app_key = "c9RZ1ZLxPe6wQVWOUwjaWOLvM7EpXHwe"

        self.get_token()

    def get_token(self):

        """
        获取token
        :return: bool
        """
        print("BaiduTts: getting token...")
        url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + self.app_id +\
              "&client_secret=" + self.app_key

        res = requests.get(url)

        if res.status_code == 200:
            self.token = res.json()["access_token"]
            print("BaiduTts: get success")
            return True
        else:
            print("BaiduTts: meet error when getting token!")
            return False

    def start(self, text):

        """
        开始合成
        :param text: 要合成的文本
        :return: bool
        """
        print("BaiduTts: requesting tts..., text: " + text)

        text = parse.quote_plus(text) # ATTENTION, error may be here
        print("urlencoded's text: ", text)

        url = "http://tsn.baidu.com/text2audio"
        param = {
            "tex": text,
            "tok": self.token,
            "cuid": "ALMS",
            "ctp": 1,
            "lan": "zh",
            "vol": 10,
            "spd": 5,
            "per": 4,
            "aue": 6
        }

        data = parse.urlencode(param)
        req = request.Request(url, data.encode('utf-8'))

        f = request.urlopen(req)
        result_str = f.read()

        headers = dict((name.lower(), value) for name, value in f.headers.items())

        if "audio" in headers["content-type"]:
            print("BaiduTts: tts requested success")
            with open("./data/audio/say.wav", "wb+") as f:
                f.write(result_str)
            self.player.say()
            return True
        else:
            print("BaiduTts: tts requested fail!")
            print(result_str)
            return False



