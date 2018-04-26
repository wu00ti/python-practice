import xlwt
import json

def write_txt_to_xls(txt_file):
    file_object = open(txt_file,'r')
    file_content = json.load(file_object)

    xls_object = xlwt.Workbook()
    sheet = xls_object.add_sheet('numbers')
    for i in range(len(file_content)):
        data =file_content[i]
        for j in range(len(data)):
            sheet.write(i,j,data[j])

    xls_object.save('numbers.xls')


if __name__ == "__main__":
    write_txt_to_xls('numbers.txt')
