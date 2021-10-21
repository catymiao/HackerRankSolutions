def swap_case(s):
    newStr = ''
    for i in s:
        if i.isupper() == True:
            newStr+=i.lower()
        else:
            newStr+=i.upper()
    return(newStr)
