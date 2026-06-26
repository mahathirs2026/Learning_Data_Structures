nums = [4, 5, 6, 5, 9, 8, 4, 9,9]

occ = {}

for key in nums:
    if key in occ:
        occ[key] +=1
    else:
        occ[key] = 1

olist = []

for i in nums:
    if occ[i] == 2:
        olist.append(i)
    else:
        continue

outlist = []
for i in range(len(olist)):
    if olist[i] in olist[:i]:
        continue
    else:
        outlist.append(olist[i])

print(outlist)
    