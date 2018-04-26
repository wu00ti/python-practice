import xlwt
import json

def write_txt_to_xls(txt_file):
    txt_object = open(txt_file,'r')
    file_content = json.load(txt_object)

    xls_object = xlwt.Workbook()
    sheet = xls_object.add_sheet('student')
    for i in range(len(file_content)):
        sheet.write(i,0,i+1)
        data = file_content[str(i+1)]
        for j in range(len(data)):
            sheet.write(i,j+1,data[j])
    xls_object.save('student.xls')


if __name__ == "__main__":
    write_txt_to_xls('student.txt')
