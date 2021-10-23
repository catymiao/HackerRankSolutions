def wrap(string, max_width):
    n= len(string)//max_width
    l=list(string)
    for i in range(1,n+1,1):
        l.insert((max_width+1)*i-1,'\n')
    return ''.join(l)


import textwrap
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
