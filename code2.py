# sort without using sort keyword

list1=[41,2,12,6,35,8,10,1,19]
n = len(list1)

for i in range(n):
    for j in range(i+1,n):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]

print(list1)
#[1,2,6,8,10,12,19,35,41]
