def insertion_sort(li):
    for i in range(1,len(li)):
        j=i-1
        val= li[i]
        while(j>=0 and val<li[j]):
            li[j+1]=li[j]
            j=j-1

        li[j+1]=val
    return li

li=[]
n=int(input("enter the no of values "))
for i in range (1,n+1) :
    li.append((int(input("enter the value "))))
    
print("the sorted a is:",insertion_sort(li))
