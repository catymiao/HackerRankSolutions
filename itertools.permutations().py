import itertools
string,k = input().split()

qualified_str = ''
for i in string:
    if i.isalpha() == True and i.isupper()==True:
        qualified_str+=i
for i in sorted(list(itertools.permutations(qualified_str,int(k)))): 
    print(''.join(i))
