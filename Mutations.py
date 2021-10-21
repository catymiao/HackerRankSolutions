# Method 1 - directly modify the string 
def mutate_string(string, position, character):
    string = string[:position] + character + string[(position+1):]
    return(string)
    
# Method 2 - convert a string to a list, then modify the list 
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return(string)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
