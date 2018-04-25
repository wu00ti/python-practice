import os
import sys

def code_lines(target_file):
    total_lines = 0
    empty_lines = 0
    comment_lines = 0

    file_object = open(target_file,'r')
    for line in file_object:
        word_list = line.split()
        if word_list == []:
            empty_lines += 1
        elif word_list[0] == '#':
            comment_lines += 1
        total_lines += 1

    file_object.close()
    return total_lines,empty_lines,comment_lines

if __name__ == "__main__":
    t_lines = 0
    e_lines = 0
    c_lines = 0
    if len(sys.argv) <= 1:
        print("Need at least 1 parameter.Try to execute 'python count_code.py $dir_path'")
    else:
        for dir_path in sys.argv[1:]:
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path,file_name)
                t,e,c = code_lines(file_path)
                t_lines += t
                e_lines += e
                c_lines += c
        print("Total lines:%s,Empty lines:%s.Comment Lines:%s." % (t_lines,e_lines,c_lines))
