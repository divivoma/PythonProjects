# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 18:53:48 2018

@author: Markos
"""

def fact(n):
    if n == 1:
        return 1
    else:
         return n*fact(n-1) #RECALL ITSELF !!

#####################################
# EXAMPLE:  testing for palindromes
#####################################
        
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

#print(isPalindrome('eve'))
#
#print(isPalindrome('Able was I, ere I saw Elba'))
#
#print(isPalindrome('Is this a palindrome'))
    
#******************************** DICTIONARY **************************
#A python dictionary stores pairs  of data : matches key to the value
#No order is guaranteed
# {key : value}

grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}
print(grades['Ana'])
grades.keys()   #must be unique
grades.values() #can be any value also list or other dictionaries! 

#####################################
# EXAMPLE: using dictionaries
#          counting frequencies of words in song lyrics
#####################################

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:      #           key       value  
            myDict[word] += 1   # mydict = {word, n_freq_word}
        else:
            myDict[word] = 1
    return myDict
    
    
she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah',
                 'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'you', 'think', "you've", 'lost', 'your', 'love',
                    'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
                    "it's", 'you', "she's", 'thinking', 'of',
                    'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',
                    
                    'she', 'says', 'she', 'loves', 'you',
                    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                    'yes', 'she', 'loves', 'you',
                    'and', 'you', 'know', 'you', 'should', 'be', 'glad',
                    
                    'she', 'said', 'you', 'hurt', 'her', 'so',
                    'she', 'almost', 'lost', 'her', 'mind',
                    'and', 'now', 'she', 'says', 'she', 'knows',
                    "you're", 'not', 'the', 'hurting', 'kind',
                    
                    'she', 'says', 'she', 'loves', 'you',
                    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                    'yes', 'she', 'loves', 'you',
                    'and', 'you', 'know', 'you', 'should', 'be', 'glad',
                    
                    'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                    'with', 'a', 'love', 'like', 'that',
                    'you', 'know', 'you', 'should', 'be', 'glad',
                    
                    'you', 'know', "it's", 'up', 'to', 'you',
                    'i', 'think', "it's", 'only', 'fair',
                    'pride', 'can', 'hurt', 'you', 'too',
                    'pologize', 'to', 'her',
                    
                    'Because', 'she', 'loves', 'you',
                    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                    'Yes', 'she', 'loves', 'you',
                    'and', 'you', 'know', 'you', 'should', 'be', 'glad',
                    
                    'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                    'with', 'a', 'love', 'like', 'that',
                    'you', 'know', 'you', 'should', 'be', 'glad',
                    'with', 'a', 'love', 'like', 'that',
                    'you', 'know', 'you', 'should', 'be', 'glad',
                    'with', 'a', 'love', 'like', 'that',
                    'you', 'know', 'you', 'should', 'be', 'glad',
                    'yeah', 'yeah', 'yeah',
                    'yeah', 'yeah', 'yeah', 'yeah'
]

beatles = lyrics_to_frequencies(she_loves_you)



def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)
    
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])  #remove word from dict
        else:
            done = True
    return result
    
print(words_often(beatles, 5))





