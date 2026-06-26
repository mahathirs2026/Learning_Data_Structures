user_input = "TabBA WAS COOL The cat and the dog"

lowcase = user_input.lower()
emptydict = {}


for key in lowcase:
    if key == " ":
        continue

    if key in emptydict:
        emptydict[key] += 1

    else:
        emptydict[key] = 1


freqnow = 0
freqold = 0
maxf = 0

for key in emptydict:
    if emptydict[key] > freqold:
        freqnow = emptydict[key]
        freqold = freqnow
        maxf = key
    else:
        freqnow = freqnow
        freqold = freqold

print(maxf , "----->" , freqnow)

    
