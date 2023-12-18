from mapper import Layouts
from typing import List

import argparse

# T_LayoutMap = Union[Layouts.Q2C, Layouts.C2D, Layouts.Q2D]


class WordFinder():
    def __init__(self, layout):
        self.__translation = layout
        self.word_list: List = []

    def add_word_if_translatable(self, word, wordbank):
        if (translated_word := self.translate_word(word)) and translated_word != '':
            if (word_exists := wordbank.get(translated_word, None)):
                self.add_word_pair(word, translated_word)

    def translate_word(self, word: str) -> bool:
        generated_chars = []
        for char in word:
            if char in self.__translation:
                generated_chars.append(self.__translation[char])
            else:
                return ''
        return ''.join(generated_chars)
    
    def add_word_pair(self, original_word: str, translated_word: str) -> None:
        self.word_list.append((original_word, translated_word))

    def get_word_pairs(self) -> List:
        return self.word_list

    def printable(self) -> str:
        return '\n'.join([', '.join(words) for words in self.word_list])
    
    def make_dict(self) -> str:
        return {word[0]: word[1] for word in self.word_list}


def find_words_in_common(args):
    layouts = Layouts(args.alphabetic)
    find_q2c = WordFinder(layouts.Q2C)
    find_c2d = WordFinder(layouts.C2D)
    find_q2d = WordFinder(layouts.Q2D)


    with open(args.filepath, "r") as wordlist:
        wordbank = {word.lower(): 1 for word in wordlist.read().split('\n')}
        print(len(wordbank))

    print("iterating through wordbank")
    for word in wordbank:
        find_q2c.add_word_if_translatable(word, wordbank)
        find_c2d.add_word_if_translatable(word, wordbank)
        find_q2d.add_word_if_translatable(word, wordbank)

    """
    q2c_dict = find_q2c.make_dict()
    c2d_dict = find_c2d.make_dict()
    q2d_dict = find_q2d.make_dict()

    
    q2c2d = []

    for val in q2c_dict.values():
        if (d_val := c2d_dict.get(val, None)):
            q2c2d.append((val, d_val))
    """

    if (args.write):
        with open("q2c.txt", "w") as f:
            f.write(find_q2c.printable())
        with open("c2d.txt", "w") as f:
            f.write(find_c2d.printable())
        with open("q2d.txt", "w") as f:
            f.write(find_q2d.printable())
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        prog='WhatsTheWordKeyboard?',
                        description='This program translates words between keyboard layouts.'
                        )
    parser.add_argument('-f', '--filename',
                        default="words.txt"
                    )      # take in a file path.
    parser.add_argument('-a', '--alphabet',
                        default=False, action='store_true'
    ) # if set, only consider alphabetic letters
    parser.add_argument('-w', '--write',
                        default=False, action='store_true'
    ) # if set, write output files.

    args = parser.parse_args()

    find_words_in_common(args)


