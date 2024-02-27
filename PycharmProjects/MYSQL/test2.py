

# l = ['sat', 'bat', 'cat', 'mat']
# test = list(map(list, l))
# print(test)

def even_or_odd(x):
    if x%2==0:
        return 'even'+str(x)
    else:
        return "odd"+str(x)
x = [1,2,3,4,5,6,7,8,9]
m = list(map(even_or_odd,x))
print(m)


print(set(x))
