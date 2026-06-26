import string


user_input = "apple, Orange, !potato ....PIZZA.?: Pineapple"

user_input = user_input + " "
low = user_input.lower()

punc = string.punctuation
word = " "
bigram = []


for char in low:
    if char in punc:
        continue
    if char != " ":
        word += char

    else :
        bigram.append(word)
        word = " "
print (bigram)
fbr = []
if len(bigram) % 2 != 0:
    for i in range(0,len(bigram)-1,2):
        fbr.append(bigram[i] + " " + bigram[i+1])
    
    fbr.append(bigram[len(bigram)-1] + " " + bigram[0])

else:
    for i in range(0,len(bigram),2):
        fbr.append(bigram[i] + " " + bigram[i+1])
        
    
print(fbr)