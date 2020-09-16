import checkingWords

def main1():
    word = input('Syötä sanasi: ')
    finnish_words = checkingWords.read_words('kotus-sanalista-suomi.txt')

    if word.lower() in finnish_words:
        print(word + ' löytyi.')
    else:
        print('Ei')

if __name__ == '__main__':
    main1()