#Hope Crisafi
#Lab 10
#6/1/21
#Grace Parker

#NJW 9.5/10

import string
import urllib.request
import ssl

#1a
def open_file(fileName):
    myFile = open(fileName, 'r')
    gettyStr = myFile.read()
    
    myFile.close()

    return gettyStr

#NJW Don't put in calls to functions if it's not asked for
gettyText = open_file('getty.txt')


#1b
def replace_punctuation(text):
    for punctuation in string.punctuation:
            text = text.replace(punctuation,"")
            #NJW This only needs to be done ONCE
            #NJW outside the loop
            text = text.lower()

    return text

   

#1d

#NJW This should ALSO print the total number of words (-0.5)
def make_dictionary(string):
    strDict = {}
    
    for word in string.split():
        
        if word in strDict:
            strDict[word] += 1
        else:
            strDict[word] = 1

    return strDict

#1f

getty = make_dictionary(gettyText)

def most_frequent_word(dictionary):
    mostFreq = 0

    for value in dictionary:
        count = dictionary[value]
        if len(value) > 5 and count > mostFreq:
            mostFreq = count
            freqWord = value
            
    print('most frequent word is ',freqWord, 'which occurs ',mostFreq, 'times.')
    return mostFreq





#1g

def lab10():
    #openFile = open_file(fileName)
    openFile = get_dracula()
    replacePunctuation = replace_punctuation(openFile)
    wordCount = make_dictionary(replacePunctuation)
    mostFrequentWord = most_frequent_word(wordCount)
    print(mostFrequentWord)




#1h

#USE THIS ONE, NOT THE SECOND ONE (unless the second one is right)
def function_H(stringDict):
    maxCount = most_frequent_word(stringDict)
    counter = 0
    words = 0

    while counter < 8:
        for words in stringDict:
            if stringDict[words] == maxCount and len(words) > 5:
                counter += 1
                #NJW Don't need the following
                if counter <= 8:
                    print(words, stringDict[words])
        maxCount -= 1
            
            

##def function_h(dictionaryOfCounts):   
##    count = 0
##    freqWord = 0
##    while count < 8:
##        mostFreq = 0
##        for value in dictionaryOfCounts:
##            count = dictionaryOfCounts[value]
##            if len(value) > 5 and count > mostFreq:
##                mostFreq = count
##                freqWord = value
##            print(freqWord, mostFreq)
##            count += 1
##            dictionaryOfCounts.pop(freqWord)


def get_dracula():
    response = urllib.request.urlopen('https://www.gutenberg.org/files/345/345-0.txt')
    data = response.read()      # a `bytes` object
    dracula_text = data.decode('utf-8')
    return(dracula_text)


















    

























    
