words = ['one','if','tree','a','.','1','one','bars','?','!','}','hello','one','tree','almighty','1230']

stopwords_file_path = 'eng_stopwords.txt'
with open(stopwords_file_path,"r") as stopwords:
    stopwords_content = stopwords.read()

stopwords = stopwords_content.splitlines()



def wordfreq(words,stopwords):
    frequencies = {}
    for word in words:
        if word not in stopwords:
            frequencies[word] = frequencies.get(word,0) + 1
    return frequencies     



print(wordfreq(words,stopwords))