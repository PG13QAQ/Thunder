b = 1
while b <= 9:
    a = 1
    while a <b:
        print(a,"x",b,"=",a*b,end='  ')
        a += 1
    print (a,"x",b,"=",a*b)
    b += 1