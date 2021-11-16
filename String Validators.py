if __name__ == '__main__':
    s = raw_input()

    n1=0
    n2=0
    n3=0
    n4=0
    n5=0
    
    for i in s:
        if i.isalnum()==True:
            n1+=1
        if i.isalpha()==True:
            n2+=1
        if i.isdigit()==True:
            n3+=1
        if i.islower()==True:
            n4+=1
        if i.isupper()==True:
            n5+=1
    if n1>= 1:
        print(True)
    else:
        print(False)
    if n2>= 1:
        print(True)
    else:
        print(False) 
    if n3>= 1:
        print(True)
    else:
        print(False) 
    if n4>= 1:
        print(True)
    else:
        print(False) 
    if n5>= 1:
        print(True)
    else:
        print(False)
        
        
