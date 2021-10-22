if __name__ == '__main__':
    s = input()
    n1=0
    n2=0
    n3=0
    n4=0
    n5=0
    
    for i in s:
        if i.isalnum()==True:
            n1+=1
    if n1>= 1:
        print(True)
    else:
        print(False)
        
    for i in s:
        if i.isalpha()==True:
            n2+=1
    if n2>= 1:
        print(True)
    else:
        print(False)    
        
    for i in s:
        if i.isdigit()==True:
            n3+=1
    if n3>= 1:
        print(True)
    else:
        print(False)    
        
    for i in s:
        if i.islower()==True:
            n4+=1
    if n4>= 1:
        print(True)
    else:
        print(False)   
        
    for i in s:
        if i.isupper()==True:
            n5+=1
    if n5>= 1:
        print(True)
    else:
        print(False)
