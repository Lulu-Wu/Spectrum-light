# 自定义函数
import time
from global_val import GlobalVal
import freq
from init import np
import show

def menu():
    if GlobalVal.mode == 2:
        print("in menu.py, current mode is freq")
        np.fill((0, 0, 0))
        while True:
            if GlobalVal.mode != 2:
                break
            freq.read()
            show.freq_show()
            freq.save()


