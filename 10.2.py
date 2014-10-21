__author__ = 'Madeleine'


#1
list = [10, 8, 17, 3, 14]

for j in range(len(list)):
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            temp=list[i]
            list[i]=list[i+1]
            list[i+1]=temp

print(list)


