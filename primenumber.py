user_list = [0, 4, 5, 6, 5, 8, 4, 9, 4, 10, 10,7, 11, 13, 15, 17, 19, 21, 23, 25, 29]

prime = []

for num in user_list:
    if num not in [0, 1]:
        for i in range(2,num):
            if (num%i) == 0:
                break
            else: 
                continue
        else:
            prime.append(num)

print(prime)