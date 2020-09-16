def binary_search(word, wordlist): # Left the licenses here, they act as a reference. This is example code from the course material.
    left = 0
    right = len(wordlist) - 1

    while left <= right:
        middle = int((left + right) / 2)
        if wordlist[middle] < word:
            left = middle + 1
        elif wordlist[middle] > word:
            right = middle - 1
        else:
            return True

    return False #python3 -m cProfile -s calls sanalistat.py TO GET DATA FROM SEARCHES. line-komento eteen.