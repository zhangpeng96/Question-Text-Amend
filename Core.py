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

def regex_matched_parser(it):
    (start, end), text, result = it.span(), it.group(), ''
    if text.strip():
        # 匹配字串前一个字符是换行符的认为是字母序号，跳过
        if it.string[start-1] != '\n':
            result = ' $' + text + '$ '
        else:
            result = text
    return result

def extract_equation(uiName):
    handle = Fun.GetElement(uiName,"Text_2")
    text = Fun.GetText(uiName,"Text_2")
    regex = r"([\d\-a-zA-Z\\\.\ \<\>\=]+)"
    try:
        selected = handle.selection_get()
        return text.replace( selected, re.sub(regex, regex_matched_parser, selected, 0, re.MULTILINE) )
    except Exception as e:
        return re.sub(regex, regex_matched_parser, text, 0, re.MULTILINE)

def inline_replace(uiName, enabled, delimiter=True):
    handle = Fun.GetElement(uiName,"Text_2")
    text = Fun.GetText(uiName,"Text_2")
    print(enabled, uiName)
    # 功能函数表映射
    fn_map = [replace_greek_letter, remarkable_unit, fix_subscript_period]
    try:
        selected = handle.selection_get()
        replaced =  selected
        for i in enabled:
            replaced = fn_map[i](replaced)
            print(i, replaced)
        result = text.replace( selected, replaced )
        return result
        # # 是否定界
        # if delimiter:
        #     return ' ${}$ '.format(result)
        # else:
        #     return result
    except Exception as e:
        result = text
        print(result)
        for i in enabled:
            result = fn_map[i](result)
            print(result)
        return result 
        # # 是否定界
        # if delimiter:
        #     return ' ${}$ '.format(result)
        # else:
            
def replace_greek_letter(string):
    greeks = {
        'α': '\\alpha', 'Π': '\\pi', 'ρ': '\\rho'
    }
    for char, text in greeks.items():
        string = string.replace(char, text)
    return string
def fix_subscript_period(string):
    return string.replace('。', r'_{0}')
def remarkable_unit(string):
    return string.replace('cm', '\\ \\mathrm{cm}')

