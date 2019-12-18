import re
ex_list_a = []
ex_list_b = []
ex_dict_b = {}
s = open('a.txt', 'r')
for line in s:
    ex_list_a.append(re.split(r'[ ]',re.sub(r'\n','',line)))
s.close()
s = open('b.txt', 'r')
for line in s:
    ex_list_b.append(re.split(r'[ ]',re.sub(r'\n','',line),maxsplit = 1))
s.close()
for i in ex_list_b:
    ex_dict_b[i[0]] = i[1]
for i in ex_dict_b.keys():
    for k in ex_list_a:
        k[1] = re.sub(i,' ' + ex_dict_b[i],k[1])
s = open('out.txt', 'w')
for i in ex_list_a:
    for k in i:
        s.write(k)
    s.write('\n')
s.close()
