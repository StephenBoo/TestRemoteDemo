# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:28:33 2020

@author: libo
"""

import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import time
import tkinter.messagebox
import os
import json

root = tk.Tk()
root.title("InfoRecord(环视)V1.1")
root.geometry("800x500")

def getData():
    '''
    得到当前时间(年-月-日)
    '''
    now_Data = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
    # now_Data = datetime.datetime.now().strftime("%Y-%m-%d")
    dataVar.set(now_Data[0:10])

def getSartTime():
    '''
    得到当前时间(时-分-秒)
    '''
    startTimeString = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
    startTimeVar.set(startTimeString[-8:])


def getEndTime():
    endTimeString = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
    endTimeVar.set(endTimeString[-8:])
    
def comfirmDigit():
    '''
    确认照度只能为数字
    '''
    try:
        float(envirIllEntry.get())
        float(parkIllEntry.get())
        float(groundIllEntry.get())
        return(True)
    except:
        tkinter.messagebox.showwarning("警告", "照度值只能为数字")
        return(False)
        
    
    
def reSet():
    
    '''重置信息, 注释的不重置'''
    
    reSetComfirm = tkinter.messagebox.askokcancel("提示", "确认重置所有信息吗？")        
    if reSetComfirm:
        #dataEntry.delete(0, "end")
        #carComb.delete(0, "end")
        #weatherComb.delete(0, "end")
        requirementComb.delete(0, "end")
        isBarrierComb.delete(0, "end")
        startTimeEntry.delete(0, "end")
        endTimeEntry.delete(0, "end")
        locationEntry.delete(0, "end")
        envirIllEntry.delete(0, "end")
        parkIllEntry.delete(0, "end")
        groundIllEntry.delete(0, "end")
        groundTypeComb.delete(0, "end")
        parkTypeComb.delete(0, "end")
        parkLineTypeComb.delete(0, "end")
        parkColorComb.delete(0, "end")
        #cityEntry.delete(0, "end")
        #recorderEntry.delete(0, "end")
        commentsEntry.delete("0.0", "end")
    else:
        tkinter.messagebox.showerror("提示","信息未重置!")
    
def getInfo():
    '''
    得到所有输入框与文本框的信息并写入json
    注意commentsEntry是Text组件的起始索引值是0.0
    '''
    inFo = {}
    inFo["采集日期"] = dataEntry.get()
    inFo["采集车辆"] = carComb.get()
    inFo["天气"] = weatherComb.get()
    inFo["采集需求类别"] = requirementComb.get()
    inFo["是否有泊车关注障碍物"] = isBarrierComb.get()
    inFo["起始时间"] = startTimeEntry.get()
    inFo["结束时间"] = endTimeEntry.get()
    inFo["采集地点"] = locationEntry.get()
    inFo["环境照度"] = envirIllEntry.get()
    inFo["库位照度"] = parkIllEntry.get()
    inFo["地面照度"] = groundIllEntry.get()
    inFo["地面类型"] = groundTypeComb.get()
    inFo["库位类型"] = parkTypeComb.get()
    inFo["库位封闭程度"] = parkLineTypeComb.get()
    inFo["库内外颜色是否一致"] = parkColorComb.get()
    inFo["采集城市"] = cityEntry.get()
    inFo["采集人"] = recorderEntry.get()
    inFo["备注"] = commentsEntry.get("0.0", "end")
    '''
    inFo["data"] = dataEntry.get()
    inFo["car"] = carComb.get()
    inFo["weather"] = weatherComb.get()
    inFo["requirement"] = requirementComb.get()
    inFo["isBarrier"] = isBarrierComb.get()
    inFo["startTime"] = startTimeEntry.get()
    inFo["endTime"] = endTimeEntry.get()
    inFo["location"] = locationEntry.get()
    inFo["envirIll"] = envirIllEntry.get()
    inFo["parkIll"] = parkIllEntry.get()
    inFo["groundIll"] = groundIllEntry.get()
    inFo["groudType"] = groundTypeComb.get()
    inFo["parkType"] = parkTypeComb.get()
    inFo["parkLine"] = parkLineTypeComb.get()
    inFo["parkColor"] = parkColorComb.get()
    inFo["city"] = cityEntry.get()
    inFo["recorder"] = recorderEntry.get()
    inFo["comments"] = commentsEntry.get("0.0", "end")
    '''
    # 1 - 检查是否有未填写
    nullValue = ''
    if "" in inFo.values():
        for a in range(0, len(inFo)):
            if list(inFo.values())[a] == "":
                nullValue += (str(list(inFo.keys())[a]) + "-")
        tkinter.messagebox.showerror("有信息未填写", nullValue + '---> 未填写!')
                #tkinter.messagebox.showerror("有信息未填写",str(list(inFo.keys())[a]) + ' --> 未填写')
    # 2 - 检查环境照度是否是数字,确认输出文件路径,重置信息
    else:
        save_path = os.path.join("D:\\InfoRecord", inFo["采集日期"] + "_" + inFo["采集车辆"].split(":")[0])
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        file_name = "_".join([inFo["采集需求类别"],inFo["采集日期"],\
                              inFo["起始时间"].replace(":", ""),\
                              inFo["结束时间"].replace(":", "")]) + ".json"
        file_path = os.path.join(save_path, file_name)
       
        comfirmIllNum = comfirmDigit()
        if comfirmIllNum:
            inFo_json_str = json.dumps(inFo, indent = 4, ensure_ascii = False)
            with open(file_path, "w", encoding = "utf-8") as json_file:
                json_file.write(inFo_json_str)
            tkinter.messagebox.showinfo("提示","已经保存!")
            reSet()
            
                                             

font_1 = tkFont.Font(family = "microsoft yahei", size = 10)

'''第一行   纵：20'''
dataLabel = tk.Label(root, text = "采集日期：", font = font_1)
dataLabel.place(x = 20, y = 20)
dataVar = tk.StringVar(value = "2001-01-01")
dataEntry = tk.Entry(root, textvariable = dataVar)
dataEntry.place(x = 95, y = 20, width = 100)
getDataBtn = tk.Button(root, text = "GetDate", cursor = "hand2", activebackground = "green", command = getData)
getDataBtn.place(x = 200, y = 20, height = 20)

carVar = tk.StringVar()
carLabel = tk.Label(root, text = "采集车辆：", font = font_1)
carLabel.place(x = 285, y = 20)
carComb = ttk.Combobox(root, textvariable = carVar,
                      value = ["BJEV:津AD58605", "ERX5:津AF02036", "VV7:苏EJZ526", "VV6:苏E9Y9W2", "MKZ:苏E6D253"])
carComb.place(x = 368, y = 20, width = 130 )

weatherLabel = tk.Label(root, text = "天气：", font = font_1)
weatherLabel.place(x = 526, y = 20)
weatherVar = tk.StringVar()
weatherComb = ttk.Combobox(root, textvariable = weatherVar, 
                       value = ["晴天", "阴天", "雨天", "夜晚低照度", "地库", "雪天(小雪低照度)", "其他恶劣天气(影响能见度)"])
weatherComb.current(0)
weatherComb.place(x = 580, y = 20)



'''第二行 纵：65'''
requirementLabel = tk.Label(root, text = "采集需求类别：", font = font_1 )
requirementLabel.place(x = 20, y = 65)
requirementVar = tk.StringVar()
requirementComb = ttk.Combobox(root, textvariable = requirementVar, 
                       value = ["Park", "OD&Freespace", "other"])
requirementComb.place(x = 110, y = 65)

isBarrierLabel = tk.Label(root, text = "是否有泊车关注障碍物：", font = font_1)
isBarrierLabel.place(x = 320, y = 65)
isBarrierVar = tk.StringVar()
isBarrierComb = ttk.Combobox(root, textvariable = isBarrierVar, 
                       value = ["有", "无"])
isBarrierComb.place(x = 480, y = 65)

'''第三行 纵：110'''
startTimeLabel = tk.Label(root, text = "起始时间：", font = font_1 )
startTimeLabel.place(x = 20, y = 110)
startTimeVar = tk.StringVar()
startTimeEntry = tk.Entry(root, textvariable = startTimeVar)
startTimeEntry.place(x = 95, y = 110, width = 100)
getStartTimeBtn = tk.Button(root, text = "GetTime", cursor = "hand2", activebackground = "green", command = getSartTime)
getStartTimeBtn.place(x = 200, y = 110, height = 20)


locationLabel = tk.Label(root, text = "采集地点：", font = font_1)
locationLabel.place(x = 526, y = 110)
locationEntry = tk.Entry(root)
locationEntry.place(x = 600, y = 110)

'''第四行 纵：155'''
envirIllLabel = tk.Label(root, text = "环境照度：", font = font_1)
envirIllLabel.place(x = 20, y = 155)
envirIllEntry = tk.Entry(root, highlightcolor = "blue")
envirIllEntry.place(x = 95, y = 155)

parkIllLabel = tk.Label(root, text = "库位照度：", font = font_1)
parkIllLabel.place(x = 273, y = 155)
parkIllEntry = tk.Entry(root)
parkIllEntry.place(x = 355, y = 155)

groundIllLabel = tk.Label(root, text = "地面照度：", font = font_1)
groundIllLabel.place(x = 526, y = 155)
groundIllEntry = tk.Entry(root)
groundIllEntry.place(x = 600, y = 155)


'''第五行 纵：200'''
groundTypeLabel = tk.Label(root, text = "地面类型：", font = font_1 )
groundTypeLabel.place(x = 20, y = 200)
groundTypeVar = tk.StringVar()
groundTypeComb = ttk.Combobox(root, textvariable = groundTypeVar, 
                       value = ["水泥地", "柏油地", "砖地", "环氧地面(反光)", "草地", "其他"])
groundTypeComb.place(x = 110, y = 200, width = 100)


parkTypeLabel = tk.Label(root, text = "库位类型：", font = font_1)
parkTypeLabel.place(x = 250, y = 200)
parkTypeVar = tk.StringVar()
parkTypeComb = ttk.Combobox(root, textvariable = parkTypeVar, 
                       value = ["水平", "垂直", "斜向"])
parkTypeComb.place(x = 330, y = 200, width = 100)

parkLineTypeLabel = tk.Label(root, text = "库位线封闭程度：", font = font_1)
parkLineTypeLabel.place(x = 460, y = 200)
parkLineTypeVar = tk.StringVar()
parkLineTypeComb = ttk.Combobox(root, textvariable = parkLineTypeVar, 
                       value = ["四边", "三边", "两边T", "两边", "纯虚线", "砖线"])
parkLineTypeComb.place(x = 570, y = 200, width = 100)



'''第六行 纵：155'''
parkColorLabel = tk.Label(root, text = "库内外颜色是否一致：", font = font_1 )
parkColorLabel.place(x = 20, y = 245)
parkColorVar = tk.StringVar()
parkColorComb = ttk.Combobox(root, textvariable = parkColorVar, 
                       value = ["是(两种颜色)", "否(两种颜色以上)"])
parkColorComb.place(x = 150, y = 245, width = 130)


cityLabel = tk.Label(root, text = "采集城市：", font = font_1)
cityLabel.place(x = 320, y = 245)
cityDefault = tk.StringVar(value = "天津")
cityEntry = tk.Entry(root, textvariable = cityDefault)
cityEntry.place(x = 390, y = 245)

recorderLabel = tk.Label(root, text = "采集人：", font = font_1)
recorderLabel.place(x = 540, y = 245)
recorderEntry = tk.Entry(root)
recorderEntry.place(x = 600, y = 245)

'''第七行 纵：80'''
commentsLabel = tk.Label(root, text = "备注栏：", font = ("Arial",20) )
commentsLabel.place(x = 20, y = 280)
commentsEntry = tk.Text(root)
commentsEntry.place(x = 20, y = 330, width = 380, height = 160)


endTimeLabel = tk.Label(root, text = "结束时间：", font = font_1)
endTimeLabel.place(x = 480, y = 350)
endTimeVar = tk.StringVar()
endTimeEntry = tk.Entry(root, textvariable = endTimeVar)
endTimeEntry.place(x = 550, y = 350, width = 100)
getEndTimeBtn = tk.Button(root, text = "GetTime", cursor = "hand2", activebackground = "green", command = getEndTime)
getEndTimeBtn.place(x = 655, y = 350, height = 20)

saveBtn = tk.Button(root, text = "保存信息至 json文件", cursor = "hand2", activebackground = "blue",  command = getInfo)
saveBtn.place(x = 480, y = 400)

emptyBtn = tk.Button(root, text = "清空信息", cursor = "hand2", activebackground = "red",  command = reSet)
emptyBtn.place(x = 640, y = 400)


savePathLabel = tk.Label(root, text = "提示：保存路径为：D:\\InfoRecord\\Data_Car\\file.json")
savePathLabel.place(x = 480, y = 450)

root.mainloop()