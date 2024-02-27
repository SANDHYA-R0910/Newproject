x=[76,45,99,12,34,8,4]
# x.sort()
# print(x)
min =x[0]
for i in range(len(x)):
    if x[i]<min:
        max=min
        min=x[i]
print(max)