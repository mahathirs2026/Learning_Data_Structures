input_list = [4, 5, 6, 5, 9, 4, 8, 4, 10, 10,6]

edict= {}

for key in input_list:
    if key in edict:
        edict[key] +=1
    else:
        edict[key] = 1

print(edict)
olist = []

for num in input_list:
    if edict[num] == 1:
        olist.append(num)
    else:
        continue

print(olist)
