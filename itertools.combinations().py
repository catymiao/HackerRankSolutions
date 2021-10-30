import itertools
string,k = input().split()

qualified_str = ''
for i in string:
    if i.isalpha() == True and i.isupper()==True:
        qualified_str+=i
for k in range(1,int(k)+1,1):
    for i in sorted(list(itertools.combinations(sorted(qualified_str),int(k)))): 
        print(''.join(i))
