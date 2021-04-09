# coding=utf-8
# author: Lan_zhijiang
# description: player
# date: 2020/10/1

import pyaudio
import wave
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class Player:

    def __init__(self):

        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(self.interface, POINTER(IAudioEndpointVolume))

    def play(self, fp): # 一定要关掉类防止占用

        """
        基本play
        :param fp: 文件路径
        :return:
        """
        p = pyaudio.PyAudio()
        try:
            wf = wave.open(fp)
        except wave.Error:
            print("Player: Cannot open the file")
            return

        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )

        data = wf.readframes(1024)
        while data != b"":
            stream.write(data)
            data = wf.readframes(1024)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def say(self):

        """
        播放say.wav
        :return:
        """
        print("Player: Now playing say.wav")
        self.play(r"./data/audio/say.wav")
        print("Player: Playing end")

    def volume_on(self):

        """
        打开声音
        :return:
        """
        self.volume.SetMute(0, None)
        self.volume.SetMasterVolumeLevel(0.0, None)
