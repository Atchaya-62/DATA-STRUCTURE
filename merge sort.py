def merge_sort(li):
    if len(li) > 1:
        mid = len(li) // 2
        left = li[:mid]
        right = li[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                li[k] = left[i]
                i += 1
            else:
                li[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            li[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            li[k] = right[j]
            j += 1
            k += 1


n=int(input("Enter length of list: "))
li=[]
for i in range(n):
    li.append(int(input("Enter a number ")))
print("Before sorting: ")
print(li)
print("After sorting: ")
merge_sort(li)
print(li)
