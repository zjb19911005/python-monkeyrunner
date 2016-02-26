#coding=utf-8
__author__ = 'Junior'
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner.easy import EasyMonkeyDevice as emd
from com.android.monkeyrunner.easy import By
import random
import sys
device= mr.waitForConnection()
easy_device = emd(device)
i= random.randint(2,100)
x=1
y=1
for y in range(i):
    easy_device.startActivity('com.shishike.calm/.calmlauncher.CalmHomeActivity_')
    mr .sleep(0.5)
    for x in range(7):
        easy_device.touch(By.id('id/eight'),md.DOWN_AND_UP)

    mr .sleep(0.2)
    easy_device.touch(By.id('id/lanucher_user_loginout'),md.DOWN_AND_UP)
    mr .sleep(0.1)
    #easy_device.touch(By.id('id/positive_button'),md.DOWN_AND_UP)
    #mr .sleep(1)
    device.touch(800,450,md.DOWN_AND_UP)
    mr .sleep(0.1)
    device.press('KEYCODE_BACK',md.DOWN_AND_UP)
    mr .sleep(1)

