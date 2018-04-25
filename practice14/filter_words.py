def filter_words(words):
    file_object = open('filtered_words.txt','r')
    filtered_words = []
    for line in file_object:
        filtered_words.append(line.strip('\n'))
    file_object.close()

    filtered = False
    for filtered_word in filtered_words:
        if filtered_word in words:
            filtered = True
            break

    if filtered is True:
        print('Freedom')
    else:
        print('Human Rights')


if __name__ == '__main__':
    while True:
        input_words = input('Input some words:')
        filter_words(input_words)
