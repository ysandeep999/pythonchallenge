__author__ = 'yalamanchili'

import nltk
from nltk.corpus import words

word_list = words.words()

#print(type(word_list))
print(len(word_list))
def big(word):
    if( word[0].isupper() and word[1].isupper() and word[2].isupper()and  word[4].isupper() and word[5].isupper() and word[6].isupper()):
        return 1
    else :
        return 0



start = 0
for word in word_list:
    if len(word) == 7 :
        if(word[0].isupper()):
            print("--",word)
        #if (word[0] == word[4] and word[1] == word[5] ):
        ##start += 1
        ##if ( big(word)) == 1 :
         ##   print(word)

       ## print(start)
