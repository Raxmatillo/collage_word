import string

text = """
♦️ 4000 Essential English Words:

📕 Book 4 | Unit 7

📑 Word list (Umumiy)

⚜account - hisob raqam
⚜architect - arxitektor, me'mor 
⚜conceal - yashirmoq
⚜crime - jinoyat
⚜deed - dalolatnoma
⚜gratitude - minnatdorchilik 
⚜habitat - yashash joyi
⚜intervene - aralashmoq
⚜landmark - belgi, oriyentir
⚜legal - qonuniy
⚜memorable - unutilmas 
⚜oblige - majbur qilmoq
⚜offence - jinoyat 
⚜proclaim - e'lon qilmoq
⚜rally - namoyish
⚜resolve - hal qilmoq
⚜resource - manba 
⚜sentence - hukm 
⚜volunteer - ko'ngilli 
⚜witness - guvoh


@Vocabulary_Essential | 4000 Essential English Words kitoblaridagi barcha so'zlar shu yerda.
"""


class WordFilter:
    def __init__(self, text: str):
        self.text = text
        self.en_list = []
        self.uz_list = []

    def split_words(self):
        split_text = self.text.split()
        end_index = split_text.index("@Vocabulary_Essential")
        all_words_list = split_text[14:end_index]
        all_words_str = " ".join(all_words_list).split(" - ")
        return all_words_str

    def list_uz_en(self):
        all_words_str = self.split_words()
        end_word = all_words_str[-1]
        for words in all_words_str:
            if words == end_word:
                self.uz_list.append(words)
                continue
            self.en_list.append(words.split()[-1][1:])
            if len(words.split()) != 1:
                self.uz_list.append(" ".join(words.split()[:-1]))
        return zip(self.en_list, self.uz_list)

# test = WordFilter(text)
# w = test.list_uz_en()
# for i in w:
#     print(i)
# tuple natija qaytadi ('account', 'hisob raqam')