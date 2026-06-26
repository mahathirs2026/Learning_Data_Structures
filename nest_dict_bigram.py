sentences = [
    "The cat and the dog",
    "The dog chased the cat",
    "Cats and dogs are friends"
]

import string

punc = string.punctuation

word = ""
cleanwordlist = []
awordlist = []
for i in sentences:
    i = i.lower()
    awordlist = []
    for j in i:
        if j in punc:
            continue
        if j != " ":
            word += j
        else:
            awordlist.append(word)
            word = ""
    awordlist.append(word)
    word = ""
    cleanwordlist.append(awordlist)
#print(cleanwordlist)

bglist= []
abglist = []
for i in cleanwordlist:
    #print(i)
    for j in range(len(i)-1):
        bg = i[j] + " "+ i[j+1]
        abglist.append(bg)
    bglist.append(abglist)
    abglist = []

#print(bglist)

fdict = {}
sdict = {}

for i in range(len(bglist)):
    for j in bglist[i]:
        if j in sdict:
            sdict[j] += 1
        else:
            sdict[j] = 1
    fdict[i] = sdict
    sdict = {}

#print(fdict)


oldmax = 0
newmax = 0

bigram = ""
for i in range(len(bglist)):
    for j in bglist[i]:
        if fdict[i][j] > oldmax:
            newmax = fdict[i][j]
            oldmax = newmax
            sentence = i
            bigram = j
        else:
            continue

#print(bigram,' appears', newmax, 'times, which is the most frequent' )

#print(fdict)
odict = {}

for i in range(len(bglist)):
    for j in bglist[i]:
        if j in odict:
            odict[j] += 1
        else:
            odict[j] = 1

#print(odict)

old_max = 0
new_max = 0
for i in odict:
    if odict[i] > old_max:
        new_max += odict[i]
        old_max = new_max
    else:
        continue


mostfreq = []

for i in odict:
    if odict[i] == new_max:
        mostfreq.append(i)
    else:
        continue

print(mostfreq, "appears", new_max, "times")