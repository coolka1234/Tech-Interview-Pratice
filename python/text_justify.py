# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

#     A word is defined as a character sequence consisting of non-space characters only.
#     Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
#     The input array words contains at least one word.

from ast import JoinedStr
from typing import List

def justify(words, maxWidth) -> List[str]:
    result : List[str] = [] 
    total_words=0
    while total_words< len(words):
        sentence=""
        sen_len=0
        words_in_sen=[]
        k=0
        last_sentence=False
        while sen_len+len(words[total_words])< maxWidth:
            words_in_sen.insert(k, words[total_words])
            sen_len+=len(words_in_sen[total_words])+1
            if len(words)==total_words:
                last_sentence=True
                break
            else:
                total_words+=1
            k+=1
        spaces=maxWidth-sen_len
        i=0
        if len(words_in_sen)==1:
            sentence=words_in_sen[0]
            while len(sentence)<maxWidth:
                sentence+=" "
        elif last_sentence:
            while len(sentence)<maxWidth:
                if(i>len(words_in_sen)):
                    sentence+=" "
                else:
                    sentence+=words_in_sen[i]+" "
                i+=1
        else: 
            word_num=1
            i=0
            k=0
            single_gap=spaces//(len(words_in_sen)-1)
            overflow=spaces%(len(words_in_sen)-1)
            while sen_len!=maxWidth:
                sentence+=words_in_sen[i]
                if(i==len(words_in_sen)-1): break
                for k in range(single_gap):
                    sentence+=" "
                    if overflow>0:
                        sentence+=" "
                        overflow-=1
                i+=1
                sen_len=len(sentence)
        result+=sentence
    return result
    




if __name__=="__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(justify(words, maxWidth))    