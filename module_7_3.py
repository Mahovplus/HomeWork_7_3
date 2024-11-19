import string
class WordFinder:
    __file_names = ()
    def __init__(self, *names):
        self.file_names =  names

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            all_words.setdefault(file, [])
            with open(file, 'r',  encoding='utf-8') as fiel:
                readable = fiel.read()
                lower_readable = readable.lower()
                with open(file, 'w',  encoding='utf-8') as fiel:
                    fiel.write(lower_readable)
                    table = str.maketrans("", "", string.punctuation)
                    new_lower_readable = lower_readable.translate(table)
                    value = new_lower_readable.split()
                    all_words['test_file.txt'] += value
        return all_words

    def find(self, word):
        dict_sought = {}
        all_words = self.get_all_words()
        for name, word_sought in all_words.items():
            for num, i in enumerate(word_sought, start=1):
                if i == word or i == word.upper() or i == word.lower():
                    dict_sought.setdefault(name, num)
        return dict_sought

    def count(self, word):
        dict_sought = {}
        all_words = self.get_all_words()
        count = 0
        for name, word_sought in all_words.items():
            for i in word_sought:
                if i.lower == word or i == word.upper() or i == word.lower():
                    count += 1
            dict_sought.setdefault(name, count)
        return dict_sought



finder2 = WordFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))