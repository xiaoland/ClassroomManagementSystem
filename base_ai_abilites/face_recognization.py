# coding=utf-8
# author: Lan_zhijiang
# date: 2020/12/6
# description: baidu face recognize

import urllib.parse
import json
import urllib
import requests
import base64


class FaceReg(object):

    def __init__(self, img_type, log):

        """
        人脸识别类
        :param img: 图片数据
        :param img_type: 图片数据类型
        :return
        """
        self.log = log

        self.img_type = img_type
        self.ak = "n8C6ht73hh75pgYUtwgbviVB"
        self.sk = "FwnT6QdW1TRvkVTNTFWuR1G6pG4vpser"
        self.token = ""

        self.get_token()

    def read_img(self, img, img_type="file_path"):

        """
        读取图片数据
        :return
        """
        if img_type == "file_path":
            file = open("./data/image/" + img, "rb")
            return_data = file.read()
            file.close()
            return return_data
        elif img_type == "file_data":
            return img
        else:
            self.log.add_log("FaceReg: image format unsupportable!", 3)
            return False

    def get_token(self):

        """
        获取token
        :return
        """
        url = 'http://openapi.baidu.com/oauth/2.0/token'

        params = urllib.parse.urlencode({'grant_type': 'client_credentials',
                                         'client_id': self.ak,
                                         'client_secret': self.sk})

        r = requests.get(url, params=params)
        try:
            r.raise_for_status()
            token = r.json()['access_token']
            self.token = token
            return token
        except requests.exceptions.HTTPError:
            self.log.add_log('FaceReg: Token request failed.', 3)

    def get_face_info(self, face):

        """
        获取人脸信息
        :param face: 人脸图片数据
        :return
        """
        url = "https://aip.baidubce.com/rest/2.0/face/v3/detect" + "?access_token=" + self.token
        headers = {"Content-Type": "application/json"}
        base64data = base64.b64encode(face)
        data = {
            "image": str(base64data, "utf-8"),
            "image_type": "BASE64",
            "face_field": "age,gender,landmark,quality,facetype"
        }

        r = requests.post(url,
                          headers=headers,
                          data=json.dumps(data))

        return r.json()

    def face_detect(self, face):

        """
        检测人脸
        :param face:
        :return:
        """
        url = "https://aip.baidubce.com/rest/2.0/face/v3/detect" + "?access_token=" + self.token
        headers = {"Content-Type": "application/json"}
        data = {
                "image": str(base64.b64encode(face), "utf-8"),
                "image_type": "BASE64"
        }

        r = requests.post(url,
                          headers=headers,
                          data=json.dumps(data))

        return r.json()

    def compare_face(self, face1, face2):

        """
        人脸比较
        :param face1: 比较人脸1
        :param face2: 比较人脸2
        :return
        """
        url = "https://aip.baidubce.com/rest/2.0/face/v3/match" + "?access_token=" + self.token
        headers = {"Content-Type": "application/json"}
        data = [
            {
                "image": str(base64.b64encode(face1), "utf-8"),
                "image_type": "BASE64"
            },
            {
                "image": str(base64.b64encode(face2), "utf-8"),
                "image_type": "BASE64"
            }
        ]

        r = requests.post(url,
                          headers=headers,
                          data=json.dumps(data))

        return r.json()

    def face_search(self, face):

        """
        人脸查找
        :param: face: 人脸图片数据
        :return
        """
        url = "https://aip.baidubce.com/rest/2.0/face/v3/search" + "?access_token=" + self.token
        headers = {"Content-Type": "application/json"}
        data = {
            "image": str(base64.b64encode(face), "utf-8"),
            "image_type": "BASE64",
            "group_id_list": "class_23"
        }

        r = requests.post(url,
                          headers=headers,
                          data=json.dumps(data))
        print(r.json())
        return r.json()

    def face_sign_up(self, face, user_id):

        """
        人脸注册
        :param face: 人脸图片数据
        :param user_id: 用户id
        :return
        """
        url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add" + "?access_token=" + self.token
        headers = {"Content-Type": "application/json"}
        data = {
            "image": str(base64.b64encode(face), "utf-8"),
            "image_type": "BASE64",
            "group_id": "class_23",
            "user_id": str(user_id)
        }

        r = requests.post(url,
                          headers=headers,
                          data=json.dumps(data))

        return r.json()




