class GlobalVal:
    freq = [0] * 7        #current freq value of seven band
    freq_prev = [0] * 7   #previous freq value of seven band
    freq_gain = 1.3       #freq soft gain value
    mode = 2              #current mode

# 定义常量类
class const:
    MIN_WIDTH_GLOABL = 0
    MIN_HEIGHT_GLOBAL = 0
    MAX_WIDTH_GLOBAL = 17
    MAX_HEIGHT_GLOBAL = 8

    MIN_WIDTH_LOCAL = 0
    MIN_HEIGHT_LOCAL = 0
    MAX_WIDTH_LOCAL = 17
    MAX_HEIGHT_LOCAL = 8

    BASE_FREQ_VALUE = 500     #freq base value

