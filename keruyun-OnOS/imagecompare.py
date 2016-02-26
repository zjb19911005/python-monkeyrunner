#coding=utf-8
__author__ = 'Junior'
# 导入此程序所需的monkeyrunner模块  
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
device = MonkeyRunner.waitForConnection()  
result = device.takeSnapShot # 将截图保存至文件  
result.writeToFile('myproject/shot1.png','png') #获取指定区域的图像(200,400,200,400)，注意两个括号 
result_static=result.getSubImage((200,400,200,400)) #获取d:\shotbegin.png这张图片 
picture = MonkeyRunner.loadImageFromFile('d:\shotbegin.png','png') #第二截图并获取相同的局部图像 
result_static2=picture.getSubImage((200,400,200,400)) #使用.sameAs()对比两张图片，并输出对比结果True或False 
end=result_static.sameAs(result_static2,1.0) 
print end