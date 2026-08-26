from typing import List

def getLength(word):
    return len(word)

def sort_words(words: List[str]) -> List[str]:
    out = words.copy()
    out.sort(key=getLength, reverse=True)
    return out


def sort_numbers(numbers: List[int]) -> List[int]:
    out = numbers.copy()
    out.sort(key=abs)
    return out


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
