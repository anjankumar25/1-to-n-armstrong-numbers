a=int(input("give:"))
for i in range(1,a+1):
    b=i
    c=0
    d=len(str(i))
    while i>0:
        e=i%10
        c=c+e**d
        i=i//10
    if b==c:
        print(f"{b} is an armstrong number")