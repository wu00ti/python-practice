import xlrd
from xml.dom import minidom,Node

def open_xls():
    excel = xlrd.open_workbook("student.xls")
    student_sheet = excel.sheet_by_name("student")
    sheet_content = {}
    for row in range(student_sheet.nrows):
        row_value = student_sheet.row_values(row)
        for i in range(len(row_value)):
            if type(row_value[i]) == float:
                row_value[i] = int(row_value[i])
        sheet_content[str(row+1)] = row_value[1:]
    return sheet_content

def build_xml(content):
    doc = minidom.Document()
    root = doc.createElement('root')
    doc.appendChild(root)
    students = doc.createElement('students')
    root.appendChild(students)
    students.appendChild(doc.createComment("学生信息表\"id\" : [名字,数学,语文,英文]"))
    students.appendChild(doc.createTextNode(str(content)))

    student_xml = open('student.xml','w')
    student_xml.write(doc.toprettyxml())
    student_xml.close()

if __name__ == '__main__':
    _content = open_xls()
    build_xml(_content)
