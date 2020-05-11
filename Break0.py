a=5
while 1:
    i=1
    while i<11:
        print("%d X %d = %d" % (a,i,a*i))
        i=i+1
    b=int(input("if  you wanna continue press a number else press 0 "))
    if b==0:
        break;
    a=a+1
