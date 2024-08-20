#Method1
"""def countsort(li):
    max1=max(li)
    count=[0]*(max1+1)
    #print(count)
    for i in li:
        count[i]+=1
    j=0
    #print(count)
    for i in range(len(count)):
        while(count[i]>0):
            li[j]=i
            count[i]-=1
            #print(count)
            j=j+1

    print("Sorted list :\n",li)

countsort([2,3,7,5,7,8,2,3,6,0])"""



#Method2

def countsort(array):
    size=len(array)
    output=[0]*size

    count=[0]*(max(array)+1)

    for i in range(0,size):
        count[array[i]]+=1
    print(count)

    for i in range(1,len(count)):
        count[i]+= count[i-1]
    print(count)

   

    i=size-1
    while(i>=0):
        #print(count[array[i]]-1)
        output[count[array[i]]-1] = array[i]
        count[array[i]]-=1
        i-=1

    for i in range(0,size):
        array[i]=output[i]

    print("Sorted array:\n",array)

countsort([2,3,7,5,7,8,2,3,6,0])

    
