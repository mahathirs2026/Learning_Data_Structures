import string 

punc = string.punctuation
user_input = "The cat and the dog, chased the cat!"
lowercase = user_input.lower()



word = []
chr = ""
for i in lowercase:
  
  if i in punc:
      continue
  if i != " ":
     chr = chr+i
  else:
     if chr != "":
        word.append(chr)
        chr = ""
if chr != "":
   word.append(chr)
print(word)

## make a bigram
bigram = []
for w in range(len(word)-1):
   br = word[w] + " " + word[w+1]
   bigram.append(br)

d = {}
for key in bigram:
   if key in d:
      d[key] +=1
   else:
      d[key] = 1

print(d)