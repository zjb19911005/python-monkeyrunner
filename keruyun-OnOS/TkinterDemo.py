#coding=utf-8
__author__ = 'Junior'
from Tkinter import *
import Tkinter as tk
#from PIL import Image, ImageTk
import tkMessageBox
import urllib
import sys
import commands
import webbrowser
import os
import time
import random
import re


def btnHelloClicked():
    name = str(entryname.get())
    if len(name)%2==0:
        tkMessageBox.showinfo('这是一个弹窗!!','%s ,经过大量科学数据证明你是一个逗比!' %(name))
        #labelHello.config(text = 'Hello,逗比')
    else:
        tkMessageBox.showinfo('这是一个弹窗!!','%s ,经过大量科学数据证明你是一个好人!' %(name))
        #labelHello.config(text = 'Hello %s' %(name))

def browser():
    search= str(entrysearch.get())
    if search=='shishike':
        webbrowser.open('http://www.baidu.com')
    else:
       tkMessageBox.showinfo('这是一个弹窗!!','密码不对,不能打开浏览器!!!请重新输入!!')

def gitclone():
    os.system('git clone http://gitlab.shishike.com/b_pos/keruyun_calm3.git \n zhengxm \n zhengxm123 ')
#    status,output = commands.getstatusoutput('git clone http://gitlab.shishike.com/b_pos/keruyun_calm3.git \n zhengxm \n zhengxm123 ')
#    for item in (output):
#            t.insert(END,item)

def gitpull():
    os.system('cd /Users/Junior.Zhu/keruyun_calm3/ \n git pull\n git merge\n ')
#    status,output = commands.getstatusoutput('cd /Users/Junior.Zhu/keruyun_calm3/ \n git pull\n git merge\n ')
#    for item in (output):
#            t.insert(END,item)


def sbyxljjc():#设备有线连接检查
    status,output = commands.getstatusoutput('adb devices')
    for item in ('adb device'):
        t.insert(END,item),
    if len(output[26:])==0:
        tkMessageBox.showinfo('这是一个弹窗!!','设备未连接,请重新连接设备')
#        for item in ('adb device'):
#            t.insert(END,item)
    else:
#        tkMessageBox.showinfo('这是一个弹窗!!设备列表如下',output[25:])#读取终端的返回值,切片处理,从25开始读取
        A=output[25:52]
        B=output[50:]
        for item in (A,B):
#            lb.insert(END,item)
            t.insert(END,item)

def sbwxlj():
    tkMessageBox.showinfo('ADB无线连接需要单独安装APK','安装软件完成后,打开软件\n把得到的IP地址输入到软件的输入框后,点击确认无线连接即OK\nAdbwireless下载地址:\nhttp://pan.baidu.com/s/1geeQ8gV\n')
    webbrowser.open('http://pan.baidu.com/s/1geeQ8gV')

def btgetip():
    ip = str(entryip.get())
    os.system('adb connect '+ip)
    for item in ('adb connect '+ip):
        t.insert(END,item),
    status, output = commands.getstatusoutput('adb connect '+ip)
#    tkMessageBox.showinfo('这是一个弹窗',output)
    for item in output:
#            lb.insert(END,item)
            t.insert(END,item)


def abdazapk():
    apkname = str(entryapkname.get())
    status,output = commands.getstatusoutput('adb install &s' %(apkname))
    for item in (output):
        t.insert(END,item)


def normalmonkey():
    os.popen('adb install /Users/Junior.Zhu/Desktop/KeruyunCalm3.apk').readlines()
    print'执行Monkey脚本'
    output = os.popen('adb shell monkey -p com.shishike.calm --pct-touch 50 --pct-trackball 20 -s 10 --throttle 200 -v %d' % (random.randint(50000, 100000))).read()  # 请手动替换-p参数后面的apk包名
    pattern = re.compile(r'FatalException', re.IGNORECASE)
    result = pattern.findall(output)
    if len(result) > 0:
        dt = time.strftime('%Y-%m-%d-%H-%M-%S')
        logfilename = "log_"  "_" + dt
        input = open('/Users/Junior.Zhu/Desktop/崩溃日志.txt' + logfilename + dt, 'w')
        input.write('执行monkey时发生crash，日志：')
        input.writelines(output)
        input.close()
        print '执行monkey时发生异常'
    print '测试完成，卸载'
    os.popen('adb uninstall com.shishike.calm')  # 请手动替换后面的apk包名



def abnormalmonkey():
    os.popen('adb install /Users/Junior.Zhu/Desktop/KeruyunCalm3.apk').readlines()
    print'执行Monkey脚本'
    output = os.popen('adb shell monkey -p com.shishike.calm --pct-touch 50 --pct-trackball 20 -s 10 --throttle 50 -v %d' % (random.randint(50000, 100000))).read()  # 请手动替换-p参数后面的apk包名
    pattern = re.compile(r'FatalException', re.IGNORECASE)
    result = pattern.findall(output)
    if len(result) > 0:
        dt = time.strftime('%Y-%m-%d-%H-%M-%S')
        logfilename = "log_"  "_" + dt
        input = open('/Users/Junior.Zhu/Desktop/崩溃日志.txt' + logfilename + dt, 'w')
        input.write('执行monkey时发生crash，日志：')
        input.writelines(output)
        input.close()
        print '执行monkey时发生异常'
    print '测试完成，卸载'
    os.popen('adb uninstall com.shishike.calm')  # 请手动替换后面的apk包名


def QDSSK1():

    os.system('touch /Users/Junior.Zhu/Desktop/monkeyrunnerlog.txt ')
    os.system('adb logcat -b main -v time > /Users/Junior.Zhu/Desktop/monkeyrunnerlog.txt')
    status,output = commands.getstatusoutput('monkeyrunner /Users/Junior.Zhu/PycharmProjects/Automation/loginandlogout.py')
    for item in (output):
            t.insert(END,item)


def QDSSK2():
    os.system('touch /Users/Junior.Zhu/Desktop/monkeyrunnerlog.txt ')
    os.system('adb logcat -b main -v time > /Users/Junior.Zhu/Desktop/monkeyrunnerlog.txt')
    status,output = commands.getstatusoutput('monkeyrunner /Users/Junior.Zhu/PycharmProjects/Automation/切换登陆账户.py')
    for item in (output):
         t.insert(END,item)

def KCBD():#快餐单个订单补打

    os.system('touch /Users/Junior.Zhu/Desktop/monkeyrunnerlog.txt ')
    os.system('adb logcat -b main -v time > /Users/Junior.Zhu/Desktop/monkeyrunnerlog.txt')
    status,output = commands.getstatusoutput('monkeyrunner /Users/Junior.Zhu/PycharmProjects/Automation/kuaicanbuda.py')
    for item in (output):
                t.insert(END,item)





root=tk.Tk()
#background_image = ImageTk.PhotoImage('/Users/Junior.Zhu/Desktop/keruyun.png')


root.resizable(width=False, height=False)
root.title('这是一个简陋的Demo程序',)

#menu_frame = tk.Frame(root)
#menu_frame.pack(fill=tk.X, side=tk.TOP)
#menu_frame.tk_menuBar('file_menu()', 'action_menu()',' help_menu()')

labelHello1 =tk.Label(root,text ='欢迎使用MonkeyRunner\n  by Junior.Zhu\n有任何问题,本人概不负责,有问题多试几次\n每次运行设备程序前,请完全注销退出账户\n默认没有开启adb logcat的命令,需要的另外说明\n目前为止如果开启logcat的命令需要强制关闭Demo程序才可以停止,请知悉',height =6, width = 55, fg = "blue",bg='yellow').pack()



frm=Frame(root)


frm_L=Frame(frm)

#frm_LL=Frame(frm_L)
e1 = StringVar()
entryname = Entry(frm_L,textvariable = e1,font=1,fg = "blue",justify=CENTER)
e1.set('Hello,')
entryname.pack(side=TOP)
btn1 =tk.Button(frm_L,text = "来测试下你的名字吧",fg = "blue",command =btnHelloClicked).pack()



e3 = StringVar()
entrysearch = Entry(frm_L,textvariable = e3,font=1,fg = "blue",justify=CENTER)
e3.set('打开浏览器需要密码:')
entrysearch.pack(side=TOP)
btn2 =tk.Button(frm_L,text = "百度一下,你就知道", fg = "blue",command =browser).pack()

#frm_LL.pack(side=LEFT)

#frm_LR=Frame(frm_L)
labelHello3 =tk.Label(frm_L,text ='****************GIT操作默认针对Mac OS**************', fg = "red").pack()

btn13 =tk.Button(frm_L,text = "GIT源码下载到电脑",command =gitclone).pack()


btn14 =tk.Button(frm_L,text = "GIT源码一键更新",command =gitpull).pack()

#frm_LR.pack(side=RIGHT)

labelHello5 =tk.Label(frm_L,text ='***********************************控制台输出窗口********************************************', fg = "green").pack()

t = Text(frm_L,bg='white',font=10,fg='black')

t.pack()
#sc=root.Scrollbar(frm_L,orient=root.VERTICAL)
#sc.config(command=sc.xview)


frm_L.pack(side=LEFT)


frm_R=Frame(frm)

labelHello2 =tk.Label(root,text ='*****************************************丅前面都是废话,以下才是你可能会用到的丅*************************************************', fg = "orange",).pack(fill=X)

labelHello4=tk.Label(frm_R,text ='********接下来我们切入正题******', fg = "blue",).pack(fill=X)
e2 = StringVar()
entryip = Entry(frm_R,textvariable = e2,font=1,fg = "red",justify=CENTER)
e2.set('在这里输入设备IP地址:')
entryip.pack()

btn9 =tk.Button(frm_R,text = "Adb无线连接(需ROOT)说明",command =sbwxlj).pack()


btn15 =tk.Button(frm_R,text = "确认adb无线连接" ,fg = "blue",command =btgetip).pack()

btn8 =tk.Button(frm_R,text = "设备USB有线连接检查",command =sbyxljjc).pack()


#e3 = StringVar()
#entryapkname = Entry(frm_R,textvariable = e3,font=1,fg = "red",justify=CENTER)
#e3.set('在这里复制并粘贴安装包的全名:')
#entryapkname.pack()

#btn18=tk.Button(frm_R,text = "ADB直接安装APK",command =abdazapk).pack()

#lb = Listbox(frm_R)
#lb.pack(fill=Y)



btn3 =tk.Button(frm_R,text = "有时间间隔的Monkey乱点操作",command =normalmonkey).pack()

btn4 =tk.Button(frm_R,text = "无时间间隔的Monkey乱点操作",command =abnormalmonkey).pack()

btn5 =tk.Button(frm_R,text = "账户的登陆与退出的随机操作",command =QDSSK1).pack()



btn6 =tk.Button(frm_R,text = "账户的切换登陆操作+随机次数",command =QDSSK2).pack()

btn7 =tk.Button(frm_R,text = "快餐订单中心的疯狂补打操作",command =KCBD).pack()

frm_R.pack(side=RIGHT)

frm.pack()

btn10 =tk.Button(root, text="退出程序,滚蛋吧,肿瘤君!!!",fg='red',command=root.quit).pack()



root.mainloop()




