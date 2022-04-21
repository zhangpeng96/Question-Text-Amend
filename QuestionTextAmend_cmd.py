#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

import Core
def ListBox_10_onSelect(event,uiName,widgetName):
    print(event)
    pass
def Button_15_onCommand(uiName,widgetName):
    text = Core.selected_crlf(uiName)
    Fun.SetText(uiName,"Text_2",text)
    print(text)
def Button_5_onCommand(uiName,widgetName):
    pass
def Button_6_onCommand(uiName,widgetName):
    text = Fun.GetText(uiName,"Text_2")
    print("pass!")
    print(text)
    Fun.SetText(uiName,"Text_2","？？？\n" + text)
def Button_11_onCommand(uiName,widgetName):
    enabled = [ i for i in  Fun.GetElement(uiName,"ListBox_10").curselection() ]
    text = Core.inline_replace(uiName, enabled)
    Fun.SetText(uiName,"Text_2", text)
def Button_14_onCommand(uiName,widgetName):
    uiEle = Fun.GetElement(uiName,"ListBox_10")
    uiEle.selection_clear(0, tkinter.END)
def Button_16_onCommand(uiName,widgetName):
    text = Core.extract_equation(uiName)
    Fun.SetText(uiName,"Text_2",text)
    # Core.inline_replace(uiName, [])
    # text = Core.fix_subscript_period(uiName)
    # Fun.SetText(uiName,"Text_2",text)
    # print(text)

