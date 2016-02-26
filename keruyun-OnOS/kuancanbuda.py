#coding=utf-8
__author__ = 'Junior'
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner.easy import EasyMonkeyDevice as emd
from com.android.monkeyrunner.easy import By
import random
import sys
device= mr.waitForConnection('abc',10)
easy_device = emd(device)
i= random.randint(2,100)
x=1
y=1
easy_device.startActivity('com.shishike.calm/.calmlauncher.CalmHomeActivity_')
mr .sleep(0.7)
easy_device.touch(By.id('id/login_select_account'),md.DOWN_AND_UP)
mr .sleep(0.1)
device.drag((680,150),(1000,150))
mr .sleep(0.2)
for x in range(7):
    easy_device.touch(By.id('id/eight'),md.DOWN_AND_UP)

mr .sleep(0.2)
device.touch(360,270,md.DOWN_AND_UP)
mr .sleep(0.7)
easy_device.touch(By.id('id/cashier_title_bar_menu_btn'),md.DOWN_AND_UP)
mr .sleep(0.5)
easy_device.touch(By.id('id/ordercenter'),md.DOWN_AND_UP)
mr .sleep(0.5)
easy_device.touch(By.id('id/payment'),md.DOWN_AND_UP)
mr .sleep(0.5)
for y in range(i):
    easy_device.touch(By.id('id/trade_center_reprint'),md.DOWN_AND_UP)
    mr .sleep(0.5)
    easy_device.touch(By.id('id/ordercenter_reprint_selectall'),md.DOWN_AND_UP)
    mr .sleep(0.2)
    easy_device.touch(By.id('id/ordercenter_reprint_reprint'),md.DOWN_AND_UP)
    mr .sleep(0.3)
