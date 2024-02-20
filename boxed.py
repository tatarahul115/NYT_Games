from itertools import permutations
from bs4 import BeautifulSoup
from requests_html import HTMLSession
script = BeautifulSoup(HTMLSession().get('https://www.nytimes.com/puzzles/letter-boxed').html.html,'html.parser').find_all('script', {'type': 'text/javascript'})[0].contents[0]

final_dict, unq_dict, unq_dict_2, unq_dict_3 = dict(), dict(), dict(), dict()
# all = list(input('Enter the letters in order: '))
all = [char for char in script[script.index('sides')+7:script.index('sides')+32].lower() if ord(char) >= 97 and ord(char) <= 122]
print('Enter the letters in order: ', str(all))

req_lis = list(set([i[:len(i)-1] for i in open(f'words.txt', 'r') if len(i[:len(i)-1]) >= 3]))

all_dict = {sorted(list(all))[i]:i+1 for i in range(12)}
sides =  [all[0:3], all[3:6], all[6:9], all[9:]]
cons = list(permutations(sides[0], 2)) + list(permutations(sides[1], 2)) + list(permutations(sides[2], 2)) + list(permutations(sides[3], 2))
cons = [''.join(i) for i in cons]
final, dou_temp = [], []
for i in all:
    cons.append(i+i)

nope = list(set('abcdefghijklmnopqrstuvwxyz').difference(set(all))) + cons

for i in req_lis:
    f = 1
    for j in nope:
        if j in i:
            f = 0
    if f:
        final.append(i)
final = sorted(final)
print('Done: final')

for i in final:
    unq_dict[i] = [len(set(i)), set(i)]
    if unq_dict[i][0] == 12:
        final_dict[i] = unq_dict[i]
unq_dict = dict(sorted(unq_dict.items(), key=lambda item: item[1][0], reverse = True))
print('Done: unq_dict')

unq_dict_keys = list(unq_dict.keys())
mini = sum(list(i[0] for i in list(unq_dict.values())))/len(unq_dict)
for i in range(len(unq_dict_keys)):
    for j in range(i, len(unq_dict_keys)):
        temp = unq_dict[unq_dict_keys[i]][1].union(unq_dict[unq_dict_keys[j]][1])
        if (mini*1.95) < len(temp) > max(len(unq_dict[unq_dict_keys[i]][1]), len(unq_dict[unq_dict_keys[j]][1]))+2:
            if unq_dict_keys[i][-1] == unq_dict_keys[j][0]:
                unq_dict_2[(unq_dict_keys[i], unq_dict_keys[j])] = [len(temp), temp]
                if len(temp) == 12:
                    final_dict[(unq_dict_keys[i], unq_dict_keys[j])] = [len(temp), temp]
            elif unq_dict_keys[j][-1] == unq_dict_keys[i][0]:
                unq_dict_2[(unq_dict_keys[j], unq_dict_keys[i])] = [len(temp), temp]
                if len(temp) == 12:
                    final_dict[(unq_dict_keys[j], unq_dict_keys[i])] = [len(temp), temp]
print('Done: unq_dict_2')

unq_dict_2_keys = list(unq_dict_2.keys())
for i in range(len(unq_dict_2_keys)):
    for j in range(i, len(unq_dict_2_keys)):
        temp = unq_dict_2[unq_dict_2_keys[i]][1].union(unq_dict_2[unq_dict_2_keys[j]][1])
        if unq_dict_2_keys[i][-1] == unq_dict_2_keys[j][0]:
            if len(temp) > max(len(unq_dict_2[unq_dict_2_keys[i]][1]), len(unq_dict_2[unq_dict_2_keys[j]][1]))+1:
                if unq_dict_2_keys[i][-1] == unq_dict_2_keys[j][0]:
                    unq_dict_3[(*unq_dict_2_keys[i][:-1], *unq_dict_2_keys[j])] = [len(temp), temp]
                    if len(temp) == 12:
                        final_dict[(*unq_dict_2_keys[i][:-1], *unq_dict_2_keys[j])] = [len(temp), temp]
                elif unq_dict_keys[j][-1] == unq_dict_keys[i][0]:
                    unq_dict_3[(*unq_dict_2_keys[j][:-1], *unq_dict_2_keys[i])] = [len(temp), temp]
                    if len(temp) == 12:
                        final_dict[(*unq_dict_2_keys[i][:-1], *unq_dict_2_keys[j])] = [len(temp), temp]
print('Done: unq_dict_3')

answer_dict = dict()
for i in final_dict.keys():
    answer_dict[i] = 0
    for j in i:
        answer_dict[i] += len(j)
answer_dict = list(dict(sorted(answer_dict.items(), key=lambda item: item[1])))

file = open('answer.txt','w')
for i in range(len(answer_dict)):
    for j in range(len(answer_dict[i])):
        file.write(answer_dict[i][j] + ', ')
    file.write('\n')
file.close()

print('All Done')
