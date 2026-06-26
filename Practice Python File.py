user_input = [4, 9, 9, 3, 7, 8]
#kist of intergers but one of them is missing

# make a ordered unique list
ordset = set(user_input)
ranlist = list(ordset)
ord_list = sorted(ranlist)


# find missing number


n = len(ord_list ) - 1



olist = list()

for i in range(n):

# multiple at start
    if ord_list[0] > 1:
        flist = list(range(1,ord_list[0]))

    a = ord_list[i+1] - ord_list[i]
    if a > 1:
        nlist = list(range(ord_list[i] + 1, ord_list[i+1]))
    else:
        continue

for i in range(len(flist)):
    olist.append(flist[i])
for i in range(len(nlist)):
    olist.append(nlist[i])

print(olist)
print(flist)
print(nlist)
outset = set(olist)
outlist = sorted(list(outset))
print(outlist)
