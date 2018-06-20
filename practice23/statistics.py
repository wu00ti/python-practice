# -*- coding=utf-8 -*-
import xlrd
import xlwt

class Statistics(object):
    def __init__(self,user):
        self.path_read = '/home/dp/python-practice/practice23/CallInfo.xls'
        self.path_save = '/home/dp/python-practice/practice23/Callinfo(1).xls'
        self.user = user
        self.work()

    def tran_time(self,time_str):
        time = time_str.replace('分','.').replace('秒','')
        temp = time.split('.')
        if len(temp) == 1:
            time = int(temp[0])
        elif len(temp) == 2:
            m = int(temp[0]) * 60
            s = int(temp[1])
            time = m + s
        return time 

    def word(self):
        wb = xlrd.open_workbook(self.path_read)
        sheets_list = wb.sheet_names()
        for sheet_name in sheets_list:
            wb_sheet = wb.sheet_by_name(sheet_name)
            print(wb_sheet)
            print(wb_sheet.nrows)
            print(wb_sheet.ncols)
            print(wb_sheet.cell_value(3,8))
            for i in range(1,wb_sheet.nrows):
                row = wb_sheet.row(i)

                time_str = row[3].value
                time = self.tran_time(time_str)
                self.user.total_time += time

                in_or_out = row[4].value
                if in_or_out == '被叫':
                    number_in = row[5].value
                    if number_in not in self.user.number_in_dict:
                        self.user.number_in_dict[number_in]=0
                    else:
                        self.user.number_in_dict[number_in] += 1
                elif in_or_out == '主叫':
                    number_out = row[5].value
                    if number_out not in self.user.number_out_dict:
                        self.user.number_out_dict[number_out] = 0
                    else:
                        self.user.number_out_dict[number_out]+= 1
            for key,val in self.user.number_in_dict.items():
                print('in',key,val)
            for key,val in self.user.number_out_dict.items():
                print('out',key,val)

class User():
    def __init__(self,name,num):
        self.name = name
        self.num = num
        self.total_time = 0
        self.most_call_out = ''
        self.most_call_in = ''
        self.number_in_dict = {}
        self.number_out_dict = {}

if __name__ == '__main__':
    user0 = User('wxl','18202666878')
    analyzer_obj0 = Statistics(user0)
    print('success')
