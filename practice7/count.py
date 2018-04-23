import sys

def word_count(file_path):
    file_object =  open(file_path,'r')

    word_num = 0
    for line in file_object:
        line_list = line.split()
        word_num += len(line_list)

    file_object.close()
    return word_num

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Need at least 1 parameter.Try to execute 'python count.py $image_path'")
    else:
        for infile in sys.argv[1:]:
            try:
                print("The total number of words is ",word_count(infile))
            except IOError:
                print("Can't open file!")
                pass
