# A function to determine whether a year is a leap year
def is_leap(year):
    
    if year%4 == 0:
        if year%100 == 0:
            if year%400 != 0: 
                leap = False 
            else: 
                leap = True 
        else:
            leap = True
    else:
        leap = False 
    
    return leap

year = int(raw_input())
print is_leap(year)
