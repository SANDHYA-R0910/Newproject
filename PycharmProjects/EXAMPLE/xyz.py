# NumList = []
# Number = int(input("Enter the Total Number of List Elements: "))
# for i in range(1, Number + 1):
#     value = int(input("Enter the Value of %d Element: " %i))
#     NumList.append(value)
# print("\nList: ", NumList)
# first = second = NumList[0]
# for j in range(1, Number):
#     if(NumList[j] > first):
#         second = first
#         first = NumList[j]
#     elif(NumList[j] > second and NumList[j] < first):
#         second = NumList[j]
# print("\nThe Largest Element in this List is: ", first)
# print("The Second Largest Element in this List is: ", second)


data = [1, 20, 3, 47, 5]

largest = 0
second_largest = 0

for a in data:
    if a > largest:
        if largest:
            second_largest = largest
        largest = a

print("second_largest: {}".format(second_largest))