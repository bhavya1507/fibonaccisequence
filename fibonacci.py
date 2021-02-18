N=int(input("Enter the number: "))
def fib(n):
    a=0
    b=1
    if(n==1):
        print(a)
    elif(n==2):
        print(a)
        print(b)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            z=a+b
            a=b
            b=z
            print(z)

fib(N)