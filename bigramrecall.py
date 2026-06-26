import string

text = "Dogs, cats... and birds! Birds?"

punc = string.punctuation
punc = punc
lowtext = text.lower()

wordlist = []
word = ""
for i in lowtext:
    if i in punc:
        continue
    if i != " ":
        word+=i
    else:
        wordlist.append(word)
        word = ""
wordlist.append(word)

#print(word)




bglist = []

for i in range(len(wordlist)-1):
    bigram = wordlist[i] +" "+ wordlist[i+1]
    bglist.append(bigram)
    

#print(bglist)

bgdict = {}

for i in bglist:
    if i in bgdict:
        bgdict[i] += 1
    else:
        bgdict[i] = 1

print(bgdict)