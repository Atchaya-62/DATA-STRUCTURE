def countsort(array,exp):
    size=len(array)
    output=[0]*size
    count=[0]*10
    for i in array:
       index=i//exp
       count[index%10]+=1
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    #i=size-1
    #while(i>=0):
    for i in range(len(array)-1,-1,-1):
        index=array[i]//exp
        output[count[index%10]-1]=array[i]
        count[index%10]-=1
        #i-=1
    for i in range (size):
        array[i]=output[i]
    print(array)

def raddixsort(array):
    exp=1
    maxi=max(array)
    while(maxi//exp>1):
        countsort(array,exp)
        exp=exp*10
    
raddixsort([170,802,45,1,22,6890,123,5678])
