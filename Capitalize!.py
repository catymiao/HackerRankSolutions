def solve(s):
    l=s.split('\\b')
    string = ''.join(l)
    new_str = ''
    
    for i in range(len(string)):
        if i == 0 or string[i-1] ==' ':
            new_str += string[i].upper()
        else:
            new_str += string[i]
    return(new_str)



# Capitalize strings like 'chris alan'
