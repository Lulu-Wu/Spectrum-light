import time
from coordinateMap import coordinate_map
from global_val import GlobalVal,const
from init import np,freq_ADC,pin_freq_rst,pin_freq_str

def read():
    pin_freq_rst.value(0)
    time.sleep(0.00001)
    pin_freq_rst.value(1)  #设置reset为高电平
    time.sleep(0.00001)  #延时10us
    pin_freq_rst.value(0) #设置reset为低电平
    time.sleep(0.0001)  #延时100us，等待设置strobe
    
    for i in range(7):
        pin_freq_str.value(1)  #设置strobe为高电平
        time.sleep(0.00005)  #延时50us
        pin_freq_str.value(0)  #设置strobe为低电平
        time.sleep(0.00004)  #延时40us
        GlobalVal.freq[i] = int(freq_ADC.read() * GlobalVal.freq_gain)
#         print("Freq i:", i, GlobalVal.freq[i])
        if GlobalVal.freq[i] > const.BASE_FREQ_VALUE:
            GlobalVal.freq[i] = (GlobalVal.freq[i] - const.BASE_FREQ_VALUE) >> 8
            if GlobalVal.freq[i] > 8:
                GlobalVal.freq[i] = 8
        else:
            GlobalVal.freq[i] = 0 #读取频段值
        time.sleep(0.00001)  #延时10us
        time.sleep(0.008)

def display(np, x, y, width, height, height_prev, direction, RGB):
    r = (RGB >> 16) & 0xFF
    g = (RGB >> 8) & 0xFF
    b = RGB & 0xFF
    if direction == 'up':
        if height > height_prev:
            for i in range(height):
                for j in range(width):
                    np[coordinate_map(x - i, y + j)] = (r, g, b)
        else:
            for i in range(const.MAX_HEIGHT_GLOBAL - height):
                for j in range(width):
                    if i != 7:
                        np[coordinate_map(i, y + j)] = (0, 0, 0)
                i= i + 1
        return np
    
def save():
    for i in range(7):
        GlobalVal.freq_prev[i] = GlobalVal.freq[i]
            