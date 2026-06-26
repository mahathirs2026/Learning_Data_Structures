user_input = [4, 5, 6, 5, 8, 4, 9, 4, 10, 10]


olist = []

for i in range(len(user_input)):
    # if there is duplicate in all places other than the last
    if user_input[i] in user_input[:i]:
        continue
    else:
        olist.append(user_input[i])

print(olist)