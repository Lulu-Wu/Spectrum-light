# 系统模块
import network
import urequests
import time
from machine import Pin,TouchPad,Timer
from neopixel import NeoPixel
from machine import ADC

from global_val import GlobalVal

# LED pin
pin_led = Pin(27, Pin.OUT)
np = NeoPixel(pin_led, 136)
# freq pin
pin_freq_out = Pin(33, Pin.IN)
freq_ADC = ADC(pin_freq_out)
freq_ADC.atten(ADC.ATTN_11DB)

pin_freq_rst = Pin(26, Pin.OUT, value = 0)
pin_freq_str = Pin(25, Pin.OUT, value = 0)