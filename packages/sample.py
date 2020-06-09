#even or odd
def even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

    
    
#average
def average(start,end):
    s=0
    count=0
    for i in range(start,end+1):
        s=s+i
        count=count+1
    print("average:",s/count)

    
    
    
#leapyears in range   
def leapyears(l,u):
    for year in range(l,u+1):
        if year%400==0 or (year%100!=0 and year%4==0):
            print(year,end=" ")

            
            
            
#prime
def prime(l,u):
    for val in range(l,u+1):
        if val>1:
            for n in range(2,val):
                if val%n==0:
            else:
                print(val)

