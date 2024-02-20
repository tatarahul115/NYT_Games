from itertools import combinations
from Levenshtein import distance as lev
req_lis, dict_req_lis = [i[:len(i)-1] for i in open(f'words.txt', 'r') if len(i[:len(i)-1]) == 5], dict()
for i in req_lis:   dict_req_lis[i] = True

# def lev_vow_def(lis):
#     vowels = 'aeiou'
#     lev_vow_dict = dict()
#     for i in range(len(lis)):
#         t = 0
#         for j in range(5):
#             if vowels[j] in lis[i]:
#                 t+=1
#         if t == 4:
#             lev_vow_dict[lis[i]] = 0

#     for i in list(lev_vow_dict):
#         for j in list(lev_vow_dict):
#             lev_vow_dict[i] += lev(i, j)

#     return lev_vow_dict

'''[('ourie', 49), ('ousia', 51), ('outie', 51), ('aurei', 54), ('ouija', 55), ('oakie', 56), ('audio', 57), ('louie', 57), ('oecia', 57), ('adieu', 59), ('auloi', 59), ('euxoa', 63), ('uraei', 64), 
('aequi', 65), ('kioea', 67), ('heiau', 68)]'''
# print(min(lev_vow_def(req_lis).items(), key = lambda item: item[1]))

def lev_atoa(inp_list):
    lev_dict = dict()

    for i in list(inp_list):
        lev_dict[i] = 0
        for j in list(inp_list):
            lev_dict[i] += lev(i, j)

    lev_dict = dict(sorted(lev_dict.items(), key=lambda item: item[1], reverse = False))
    return lev_dict

tries = 1
while tries <= 5:
    n = len(req_lis)
    
    while True:
        inp = input('Enter your word: ')
        if len(inp) == 5:
            break

    while True:
        inp_st = input('Enter the status: ')
        if len(inp_st) == 5:
                break
    if inp_st == 'ggggg':
        break
    
    for i in range(5):
        if inp_st[i] == 'o':
            for j in range(n):
                if req_lis[j][i] == inp[i] or inp[i] not in req_lis[j]:
                    dict_req_lis[req_lis[j]] = False
        elif inp_st[i] == 'r':
            for j in range(n):
                if inp[i] in req_lis[j]:
                    dict_req_lis[req_lis[j]] = False
        else:
            for j in range(n):
                if req_lis[j][i] != inp[i]:
                    dict_req_lis[req_lis[j]] = False

    req_lis = list(dict(i for i in dict_req_lis.items() if i[1]))

    file = open('answer.txt','w')
    for key, value in lev_atoa(req_lis).items():  
        file.write(f'{key}:{value}\n')
    file.close()

    print(tries, inp, inp_st)
    
    tries += 1

print('Challenge Completed')