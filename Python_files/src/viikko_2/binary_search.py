from binary_search import binary_search # Unable to determine this.

#def binary_search(word, kotus-sanalista-suomi.txt):
#   left = 0
#    right = len(list_of_words) - 1
#
#    while left <= right:
#        middle = int((left + right) / 2)
#        if list_of_words[middle] < word:
#            left = middle + 1
#        elif list_of_words[middle] > word:
#            right = middle - 1
#        else:
#            return True
#
#    return False

def read_words(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()


def main():
    finnish_words = read_words('kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')

    for word in finnish_words:
        if binary_search(word, english_words):
            print(word)


if __name__ == '__main__':
    main()

