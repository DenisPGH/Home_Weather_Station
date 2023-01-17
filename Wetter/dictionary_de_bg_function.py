from sqlite_db__function import SQLiteSensor
from variables_function import Variables


class Translate(Variables):
    def __init__(self):
        super().__init__()
        self.db = SQLiteSensor()
        self.found_new_word={}


    def collect_new_words(self,dictionary_DE_BG:dict):
        res = self.db.return_info_for_period('info', self.db.NAME_TABLE_OUTSIDE, 10)[1]
        for word in res:
            if word not in dictionary_DE_BG and word != None:
                dictionary_DE_BG[word.replace(":", "")] = ''
                self.DE_to_BG[word.replace(":", "")] = ''
        print(self.DE_to_BG)
        #return dictionary_DE_BG

    def collect_new_words_2(self):
        """
        get all new german words from the wetter outside table and print it
        :return: only the new found words
        """
        res = self.db.return_info_for_period('info', self.db.NAME_TABLE_OUTSIDE, 10)[1]
        for word in res:
            if word not in self.DICTIONARY_DE_to_BG and word != None:
                self.DICTIONARY_DE_to_BG[word] = ''
                self.found_new_word[word] = ''

        return self.found_new_word



if __name__=="__main__":
    t=Translate()
    new_words=t.collect_new_words_2()
    print(new_words)