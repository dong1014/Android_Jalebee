#coding=utf-8
import os
import time
import csv

class App:
    def __init__(self):
        self.content=""
        self.startTime=0

     #启动APP
    def launchApp(self):
        cmd='adb shell am start -W -n com.ushow.android.jalebee/com.ushowmedia.starmaker.activity.SplashActivity'
        self.content=os.popen(cmd)
    #关闭APP
    def stopApp(self):
        cmd="adb shell am force-stop com.ushow.android.jalebee"
        os.popen(cmd)
    #获取启动时间
    def getLaunchTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime=line.split(":")[1]
                break
        return  self.startTime

class Controller:
    def __init__(self,count):
        self.app=App()
        self.counter=count
        self.data=[("currenttime","thistime")]

    #单次测试过程
    def testProcess(self):
        currenttime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        self.app.launchApp()
        time.sleep(5)
        thistime=self.app.getLaunchTime()
        self.app.stopApp()
        time.sleep(2)
        self.data.append((currenttime,thistime))
    #多次执行
    def run(self):
        while self.counter >0:
            self.testProcess()
            self.counter -=1
    #写入文件
    def saveToCsv(self):
        csvfile=open("startTime.csv","w")
        write=csv.writer(csvfile)
        write.writerows(self.data)
        csvfile.close()

if __name__ == '__main__':
    contorller=Controller(3)
    contorller.run()
    contorller.saveToCsv()





