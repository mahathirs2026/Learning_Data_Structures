user_input = "The Cat"
lowercase = user_input.lower()

charlist = []

for ch in lowercase:
    if ch == " ":
        continue
    else:
        charlist.append(ch)

#print(charlist)

# make big rams
bigram = []
for i in range(len(charlist)-1):
    chr = charlist[i]+ charlist[i+1]
    bigram.append(chr)
    char = ""

#print(bigram)

dict = {}

for key in bigram:
    dict[key] = dict.get(key,0)+1

print(dict)