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

def commas_fullchar(uiName):
    handle = Fun.GetElement(uiName,"Text_2")
    text = Fun.GetText(uiName,"Text_2")
    fn = lambda x: x.replace(',', '，').replace('?', '？').replace(';', '；').replace('(', '（').replace(')', '）')
    try:
        selected = handle.selection_get()
        return text.replace( selected, fn(selected) )
    except Exception as e:
        return fn(text)

def dot_period(uiName):
    handle = Fun.GetElement(uiName,"Text_2")
    text = Fun.GetText(uiName,"Text_2")
    fn = lambda x: x.replace('。', '．').replace(' 、', '、').replace('、 ', '、').replace(' ，', '，').replace('， ', '，').replace(' 。', '。').replace('。 ', '。')
    try:
        selected = handle.selection_get()
        return text.replace( selected, fn(selected) )
    except Exception as e:
        return fn(text)

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
    text = text.replace('\nA.', '\nＡ').replace('\nB.', '\nＢ').replace('\nC.', '\nＣ').replace('\nD.', '\nＤ')
    regex = r"([\d\-a-zA-Z\\\.\ \<\>\=\{\}\_\/]+)"
    try:
        selected = handle.selection_get()
        text = text.replace( selected, re.sub(regex, regex_matched_parser, selected, 0, re.MULTILINE) )
        text = text.replace('\nＡ', '\nA.').replace('\nＢ', '\nB.').replace('\nＣ', '\nC.').replace('\nＤ', '\nD.')
        return text
    except Exception as e:
        text = re.sub(regex, regex_matched_parser, text, 0, re.MULTILINE)
        text = text.replace('\nＡ', '\nA.').replace('\nＢ', '\nB.').replace('\nＣ', '\nC.').replace('\nＤ', '\nD.')
        return text

def inline_replace(uiName, enabled, delimiter=True):
    handle = Fun.GetElement(uiName,"Text_2")
    text = Fun.GetText(uiName,"Text_2")
    # 功能函数表映射
    fn_map = [replace_greek_letter, remarkable_unit, fix_subscript_period]
    result = text
    for i in enabled:
        result = fn_map[i](result)
        print(result)
    return result
            
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
    return string.replace('cm', '\\ \\mathrm{cm}').replace('N/kg', '\\ \\mathrm{N/kg}')

