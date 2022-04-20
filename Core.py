import Fun
import re

def selected_crlf(uiName):  
    handle = Fun.GetElement(uiName,"Text_2")
    text = Fun.GetText(uiName,"Text_2")
    try:
        selected = handle.selection_get()
        return text.replace( selected, trim_crlf(selected) )
    except Exception as e:
        return trim_crlf(text)

def trim_crlf(string):
    return string.replace('\n', '').replace('\n', '')

def replace_greek_letter(string):
    greeks = {
        'α': '\\alpha', 'Π': '\\pi', 
    }
