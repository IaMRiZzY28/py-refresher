def num_1(a):
    q=[500,200,100,50,20,10,5]
    x=0
    for i in range(7):
        h=q[i]
        x=a//h
        print("notes:{}-{}".format(h,x))
        a=a%h

amg=int(input("enter a number"))
num_1(amg)