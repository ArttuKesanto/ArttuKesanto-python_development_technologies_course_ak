def read_words(
        file_path):  # Left the licenses here, they act as a reference. This is example code from the course material.
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()


def main():
    finnish_words = read_words('kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')

    # print(len(finnish_words)/2)

    for word in finnish_words:  # Tehdään 94 xxx kertaa.
        if word in english_words:  # Tehdään jopa 102 xxx kertaa. Vertailuoperaatoita voi olla 10 000 000 000 kertaa.
            print(word)


if __name__ == '__main__':
    main()
