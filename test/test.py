

import collections
from tkinter import messagebox

# def test(date):
#
#     for key in date:
#         print("{}: {}".format(key, date[key]))

def displayOperationHo ur(date):
    # display = OperationHour.display_Subway_OperationHour()
    # for key in date:
    # print("{}: {}".format(key, date[key]))
    # messagebox.showinfo(message=date.values().)
    list1 = ['a','b','c']
    list2 = ['a:1','b:2','c:3']
    thisdict = {
        "Weekdays":"     8am - 20.30pm",
        "Saturday": "     8am - 18.30pm",
        "Sunday & PH": '  8am - 18pm'
    }
    # messagebox.showinfo('Results',list2)
    messagebox.showinfo('Results', '\n'.join("".join(format(key) for key in list2)))
    #     messagebox.showinfo(message="{}: {}".format(key, date[key]))

def display_Subway_OperationHour():
    thisdict = {
        "Weekdays":"     8am - 20.30pm",
        "Saturday": "     8am - 18.30pm",
        "Sunday & PH": '  8am - 18pm'
    }
    subwayDisplay = collections.OrderedDict(thisdict)
    displayOperationHour(subwayDisplay)

display_Subway_OperationHour()