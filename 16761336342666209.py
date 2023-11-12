from collections import OrderedDict
vote_num = int(input())
country_lis =[]
counter = OrderedDict()
for i in range(vote_num):
    country = str(input())
    country_lis.append(country)
for letter in country_lis:
    counter[letter] = counter.get(letter,0) + 1
moratab = list(counter.keys())
moratab = sorted(moratab)
for j in moratab:
    print(j,counter[j])

