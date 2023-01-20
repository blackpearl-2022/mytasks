a=int(input("enter a number of rows :"))
row = 0
while row<a:
    space = a-row-1
    while space>0:
        print(end=" ")
        space = space-1
    star = row+1
    while star>0:
        print ("*",end=" ")
        star = start-1
    row = row+1
    print()


