# coding=utf-8
# author: Lan_zhijiang
# date: 2020/12/6
# description: opencv camera operations

import cv2


class CameraManager:

    def __init__(self, log, camera_id=0, camera_resolution=(1280, 720)):

        self.log = log

        self.camera_id = camera_id
        self.camera = cv2.VideoCapture(self.camera_id, cv2.CAP_DSHOW)
        self.camera.set(3, camera_resolution[0])
        self.camera.set(4, camera_resolution[1])

    def capture_image(self, fn="img.jpg", face=True):

        """
        拍照
        :param fn: 文件名
        :param face
        :return:
        """
        self.log.add_log("CameraManager: capturing one image...", 1)

        a, img = self.camera.read()
        cv2.imwrite("./data/image/" + fn, img)

        return img

    def capture_video(self, fn="video.avi", size=(1280, 720)):

        """
        录制视频
        :param fn: 文件名
        :param size: 帧大小
        :return:
        """
        self.log.add_log("CameraManager: capturing one video...", 1)
        writer = cv2.VideoWriter("./data/video/" + fn, cv2.VideoWriter_fourcc(*'MJPG'), 30.0, size)

        while self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                writer.write((frame))
                cv2.imshow('Now capturing...', frame)
                if cv2.waitKey(25) == ord('q'):
                    break
            else:
                break

        writer.release()
        cv2.destroyAllWindows()
        self.log.add_log("CameraManager: captured", 1)

    def show_image(self, img):

        """
        显示图片
        :param img: 要显示的图片 opencv2 image object
        :return:
        """
        cv2.imshow("image viewing", img)
        if cv2.waitKey(25) == ord("q"):
            cv2.destroyAllWindows()

