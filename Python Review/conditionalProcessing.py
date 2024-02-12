import math

def intGrid():
    n = int(input())
    grid = [ [0]*n for i in range(n)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            grid[i-1][j-1] = i*j    
    for row in grid:
        print(row)

def heronianTriangle():
    n = 100
    count=0
    for a in range(1,n+1):
        for b in range(a,n+1):
            for c in range(b,n+1):
                s = (a+b+c)/2
                try:
                    area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
                    if area.is_integer() and area<2000 and area>0:
                        print(a,b,c,area)
                        count+=1
                except ValueError as e:
                    pass
                    #print("Error: ",e)
    return count

print(heronianTriangle())

# a = 1
# b = 1
# c = 4
# s = (a+b+c)/2
# area = math.sqrt((s*(s-a)*(s-b)*(s-c)))

# print(s,type(s))
# print(area,type(area))
                 