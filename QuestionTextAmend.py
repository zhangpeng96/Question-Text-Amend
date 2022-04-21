#coding=utf-8
#import libs 
import sys
import QuestionTextAmend_cmd
import QuestionTextAmend_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  QuestionTextAmend:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = QuestionTextAmend_sty.SetupStyle()
        if isTKroot == True:
            root.title("文本快速编辑器")
            root.resizable(False,False)
            Fun.CenterDlg(uiName,root,800,540)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 800,height = 540)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Text_2 = tkinter.Text(Form_1)
        Fun.Register(uiName,'Text_2',Text_2,'text')
        Fun.SetControlPlace(uiName,'Text_2',10,10,570,520)
        Text_2.configure(relief = "sunken")
        LabelFrame_3 = tkinter.LabelFrame(Form_1,text="Text",takefocus = True,width = 10,height = 4)
        Fun.Register(uiName,'LabelFrame_3',LabelFrame_3,'frame_1')
        Fun.SetControlPlace(uiName,'LabelFrame_3',590,10,200,130)
        LabelFrame_3.configure(relief = "groove")
        Button_15 = tkinter.Button(LabelFrame_3,text="单行",width = 10,height = 4)
        Fun.Register(uiName,'Button_15',Button_15)
        Fun.SetControlPlace(uiName,'Button_15',8,8,70,28)
        Button_15.configure(command=lambda:QuestionTextAmend_cmd.Button_15_onCommand(uiName,"Button_15"))
        LabelFrame_4 = tkinter.LabelFrame(Form_1,text="符号调整",takefocus = True,width = 10,height = 4)
        Fun.Register(uiName,'LabelFrame_4',LabelFrame_4,'frame_2')
        Fun.SetControlPlace(uiName,'LabelFrame_4',590,150,200,70)
        LabelFrame_4.configure(relief = "groove")
        Button_5 = tkinter.Button(LabelFrame_4,text="圆点句号",width = 10,height = 4)
        Fun.Register(uiName,'Button_5',Button_5,'btn_period')
        Fun.SetControlPlace(uiName,'Button_5',98,8,85,30)
        Button_5.configure(command=lambda:QuestionTextAmend_cmd.Button_5_onCommand(uiName,"Button_5"))
        Button_5_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=9,weight='normal',slant='roman',underline=0,overstrike=0)
        Button_5.configure(font = Button_5_Ft)
        Button_6 = tkinter.Button(LabelFrame_4,text="标点全角",width = 10,height = 4)
        Fun.Register(uiName,'Button_6',Button_6,'btn_fullchar')
        Fun.SetControlPlace(uiName,'Button_6',8,8,85,30)
        Button_6.configure(command=lambda:QuestionTextAmend_cmd.Button_6_onCommand(uiName,"Button_6"))
        LabelFrame_8 = tkinter.LabelFrame(Form_1,text="",takefocus = True,width = 10,height = 4)
        Fun.Register(uiName,'LabelFrame_8',LabelFrame_8)
        Fun.SetControlPlace(uiName,'LabelFrame_8',590,480,200,50)
        LabelFrame_8.configure(relief = "flat")
        Button_9 = tkinter.Button(LabelFrame_8,text="粘贴",width = 10,height = 4)
        Fun.Register(uiName,'Button_9',Button_9,'btn_paste')
        Fun.SetControlPlace(uiName,'Button_9',108,8,85,34)
        Button_9.configure(bg = "#aa0000")
        Button_9.configure(fg = "#ffffff")
        Button_9.configure(activebackground = "#c40000")
        Button_9.configure(activeforeground = "#ffffff")
        Button_9.configure(relief = "flat")
        Button_7 = tkinter.Button(LabelFrame_8,text="复制",width = 10,height = 4)
        Fun.Register(uiName,'Button_7',Button_7,'btn_copy')
        Fun.SetControlPlace(uiName,'Button_7',8,8,85,34)
        Button_7.configure(bg = "#00608e")
        Button_7.configure(fg = "#ffffff")
        Button_7.configure(activebackground = "#0080c0")
        Button_7.configure(activeforeground = "#ffffff")
        Button_7.configure(relief = "flat")
        Fun.SetRoundedRectangle(Button_7,0,0)
        LabelFrame_13 = tkinter.LabelFrame(Form_1,text="行内替换",takefocus = True,width = 10,height = 4)
        Fun.Register(uiName,'LabelFrame_13',LabelFrame_13)
        Fun.SetControlPlace(uiName,'LabelFrame_13',590,230,200,190)
        LabelFrame_13.configure(relief = "groove")
        ListBox_10 = tkinter.Listbox(LabelFrame_13)
        Fun.Register(uiName,'ListBox_10',ListBox_10)
        Fun.SetControlPlace(uiName,'ListBox_10',8,8,120,150)
        ListBox_10.configure(selectmode = "multiple")
        ListBox_10.insert(tkinter.END,"希腊字母")
        ListBox_10.insert(tkinter.END,"显著单位")
        ListBox_10.insert(tkinter.END,"句号修正下标")
        ListBox_10_Scrollbar = tkinter.Scrollbar(ListBox_10,orient=tkinter.VERTICAL)
        ListBox_10_Scrollbar.place(x = 100,y = 0,width = 20,height = 150)
        ListBox_10_Scrollbar.config(command = ListBox_10.yview)
        ListBox_10.config(yscrollcommand = ListBox_10_Scrollbar.set)
        Button_11 = tkinter.Button(LabelFrame_13,text="直接",width = 10,height = 4)
        Fun.Register(uiName,'Button_11',Button_11)
        Fun.SetControlPlace(uiName,'Button_11',138,48,50,30)
        Button_11.configure(command=lambda:QuestionTextAmend_cmd.Button_11_onCommand(uiName,"Button_11"))
        Button_14 = tkinter.Button(LabelFrame_13,text="不选",width = 10,height = 4)
        Fun.Register(uiName,'Button_14',Button_14)
        Fun.SetControlPlace(uiName,'Button_14',138,128,50,30)
        Button_14.configure(command=lambda:QuestionTextAmend_cmd.Button_14_onCommand(uiName,"Button_14"))
        Button_12 = tkinter.Button(LabelFrame_13,text="定界",width = 10,height = 4)
        Fun.Register(uiName,'Button_12',Button_12)
        Fun.SetControlPlace(uiName,'Button_12',138,88,50,30)
        Button_16 = tkinter.Button(LabelFrame_13,text="公式",width = 10,height = 4)
        Fun.Register(uiName,'Button_16',Button_16,'btn_equation')
        Fun.SetControlPlace(uiName,'Button_16',138,8,50,30)
        Button_16.configure(command=lambda:QuestionTextAmend_cmd.Button_16_onCommand(uiName,"Button_16"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = QuestionTextAmend(root)
    root.mainloop()
