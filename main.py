# Remove the duplicate elements from the list

lis1 = [10,5,4,2,5,10,8,9,2,8,10]
lis2 = []
for i in lis1:
    if i not in lis2:
        lis2.append(i)
print(lis2)