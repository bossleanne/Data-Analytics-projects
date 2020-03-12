import csv
import datetime

# csvfile = open('/Users/leanne/Downloads/test.csv', 'r')

def find_value(week,opeartiontime):
    with open('/Users/leanne/Downloads/test.csv') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            # print(row)
            id = row['Routine']
            if id == week:
                if opeartiontime < row['Open'] and opeartiontime > row['Close']:
                    return 0
                    # print('closed!!')
                else:
                    return 1
                    # print('open!')

def time_split(current_date):

    day_of_week = current_date.date().strftime('%A')
    time = str(current_date.time())
    find_value(day_of_week,time)
    print(datetime.datetime.now())
    # print(day_of_week,time)

time_split(datetime.datetime.now())

# def Convert(lst):
#     res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
#     return res_dct
#
# with open("/Users/leanne/Downloads/perationHour.txt")as myFile:
#     oc = []
#     for line in myFile:
#         time_split = line.split(':')
#         oc = Convert(time_split)
#         print(oc['Weekdays'])
