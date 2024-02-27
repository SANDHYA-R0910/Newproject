x=int(input("enter num"))
for i in range(x):
    if i<=3:
        n=i
    else:
        n=x-i
    print(("ineuron "*n).center(50," "))
