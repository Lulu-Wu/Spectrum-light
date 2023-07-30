# 显示
import time
from init import np,freq_ADC,pin_freq_rst,pin_freq_str
import freq
from global_val import GlobalVal
from coordinateMap import coordinate_map

color_map = {'red': 0x0F0000, 'orange':0x7E0F00, 'yellow':0x0F0F00, 'green':0x000F00,\
             'blue':0x000E23, 'indigo':0x0E2323, 'purple':0x0E002A, 'person':0x004B0F}

date_color_map = {0:{0:0x000701, 1:0x000701, 2:0x000701, 3:0x000701, 4:0x000701, 5:0x000701,\
                     6:0x000701, 7:0x000701, 8:0x000701, 9:0x000701,\
                     'colon':0x050200, 'today':0x030300, 'nontoday':0x030003},\
                  1:{0:0x050000, 1:0x050000, 2:0x050000, 3:0x050000, 4:0x050000, 5:0x050000,\
                     6:0x050000, 7:0x050000, 8:0x050000, 9:0x050000,\
                     'colon':0x000300, 'today':0x040404, 'nontoday':0x000200},\
                  2:{0:0x000106, 1:0x000106, 2:0x000106, 3:0x000106, 4:0x000106, 5:0x000106,\
                     6:0x000106, 7:0x000106, 8:0x000106, 9:0x000106,\
                     'colon':0x060100, 'today':0x060100, 'nontoday':0x010007},\
                  3:{0:0x060100, 1:0x060100, 2:0x060100, 3:0x060100, 4:0x060100, 5:0x060100,\
                     6:0x060100, 7:0x060100, 8:0x060100, 9:0x060100,\
                     'colon':0x010501, 'today':0x010501, 'nontoday':0x010004},\
                  4:{0:0x020006, 1:0x020006, 2:0x020006, 3:0x020006, 4:0x020006, 5:0x020006,\
                     6:0x020006, 7:0x020006, 8:0x020006, 9:0x020006,\
                     'colon':0x030300, 'today':0x030300, 'nontoday':0x050202},\
                  5:{0:0x060000, 1:0x000500, 2:0x060101, 3:0x000501, 4:0x060100, 5:0x010206,\
                     6:0x000006, 7:0x050500, 8:0x060003, 9:0x000603,\
                     'colon':0x040404, 'today':0x020300, 'nontoday':0x040404}}

def freq_show():
    global np
    global people_count
    
    np = freq.display(np, 7, 0, 2, int(GlobalVal.freq[0]), int(GlobalVal.freq_prev[0]), 'up', color_map['red'])
    np = freq.display(np, 7, 2, 2, int(GlobalVal.freq[1]), int(GlobalVal.freq_prev[1]), 'up', color_map['orange'])
    np = freq.display(np, 7, 4, 2, int(GlobalVal.freq[2]), int(GlobalVal.freq_prev[2]), 'up', color_map['yellow'])
    np = freq.display(np, 7, 6, 2, int(GlobalVal.freq[3]), int(GlobalVal.freq_prev[3]), 'up', color_map['green'])
    np = freq.display(np, 7, 8, 2, int(GlobalVal.freq[4]), int(GlobalVal.freq_prev[4]), 'up', color_map['blue'])
    np = freq.display(np, 7, 10, 2, int(GlobalVal.freq[5]), int(GlobalVal.freq_prev[5]), 'up', color_map['indigo'])
    np = freq.display(np, 7, 12, 2, int(GlobalVal.freq[6]), int(GlobalVal.freq_prev[6]), 'up', color_map['purple'])
    
    np.write()