import xlwt
import json

def write_txt_to_xls(file_txt):
    file_object = open(file_txt,'r')
    file_content = json.load(file_object)

    xls_object = xlwt.Workbook()
    sheet = xls_object.add_sheet('city')
    for i in range(len(file_content)):
        sheet.write(i,0,i+1)
        data =file_content[str(i+1)]
        sheet.write(i,1,data)

    xls_object.save('city.xls')

if __name__ == "__main__":
    write_txt_to_xls('city.txt')

