#average
def average(start,end):
    s=0
    count=0
    for i in range(start,end+1):
        s=s+i
        count=count+1
    print("average:",s/count)
    
    
#even or odd
def even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
    
    
#leapyears in range   
def leapyears(l,u):
    for year in range(l,u+1):
        if year%400==0 or (year%100!=0 and year%4==0):
            print(year,end=" ")
            
            
                      
#factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact



def unique(l):
    li=[]
    for i in l:
        if l.count(i)==1:
            li.append(i)
    print(li)

def duplicates(l):
    li=[]
    for i in l:
        if i not in li:
            li.append(i)
    print(li)
