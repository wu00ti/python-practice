def filter_words(words):
    file_object = open('filtered_words.txt','r')
    filtered_words = []
    for line in file_object:
        filtered_words.append(line.strip('\n'))
    file_object.close()

    for filtered_word in filtered_words:
        if filtered_word in words:
            words = words.replace(filtered_word,'*'*len(filtered_word))

    print(words)

if __name__ == '__main__':
    while True:
        input_words = input('Input some words:')
        filter_words(input_words)
