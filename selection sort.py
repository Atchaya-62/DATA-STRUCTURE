def selection_sort(li):
    for i in range(0,len(li)):
        mini=i
        for k in range(i+1,len(li)):
            if (li[mini]>li[k]):
                mini=k

        temp=li[i]
        li[i]=li[mini]
        li[mini]=temp

    return li


li=[]
n=int(input("enter the no of values "))
for i in range (1,n+1) :
    li.append((int(input("enter the value "))))
    
print("the sorted a is:",selection_sort(li))
