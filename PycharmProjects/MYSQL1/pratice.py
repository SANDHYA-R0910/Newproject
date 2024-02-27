string = "ABCDA"
duplicates = []
for char in string:
   if string.count(char) > 1:
       if char not in duplicates:
           duplicates.append(char)
print(*duplicates)

# x="ABCB"
# y=[]
# for i in x:
#     if i == "A":
#         y.append(i)
# print(y)


