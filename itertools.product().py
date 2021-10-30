import itertools
storage1 = set(input().split());
storage1=sorted(list(map(int,storage1)))
#print(storage1)
storage2 = set(input().split());
storage2=sorted(list(map(int,storage2)))
#print(storage2)
for i in list(itertools.product(storage1,storage2)):
    print(i,end=" ") #print in one line
