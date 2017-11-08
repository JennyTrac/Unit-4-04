# Created by Jenny Trac
# Created on Nov 6 2017
# Program converts a level mark to a percent

import ui

def convert_mark(level):
    # converts level to percent
    
    if level == "NE":
        mark = 0
        return mark
    
    elif level == "R":
        mark = 30
        return mark
    
    elif level == "1-":
        mark = 53
        return mark
    
    elif level == "1":
        mark = 55
        return mark
    
    elif level == "1+":
        mark = 58
        return mark
    
    elif level == "2-":
        mark = 63
        return mark
    
    elif level == "2":
        mark = 65
        return mark
    
    elif level == "2+":
        mark = 68
        return mark
    
    elif level == "3-":
        mark = 73
        return mark
    
    elif level == "3":
        mark = 75
        return mark
    
    elif level == "3+":
        mark = 78
        return mark
    
    elif level == "4-":
        mark = 85
        return mark
    
    elif level == "4":
        mark = 90
        return mark
    
    elif level == "4+":
        mark = 95
        return mark
        
    else:
        return -1

def convert_touch_up_inside(sender):
    # button to convert
    
    level_input = str(view['mark_textfield'].text)
    converted_mark = convert_mark(level_input)
    
    view['answer_label'].text = str(converted_mark) + "%"

view = ui.load_view()
view.present('sheet')
