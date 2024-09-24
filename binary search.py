def binary_search (s, e, li, se):
    mid= (s +  e)//2
    if se in li:
        
        if li[mid]==se:
            return mid
        elif li[mid]>se:
            return binary_search (s, mid, li, se)
        elif li[mid]<se:
            return binary_search (mid+1, e, li, se)
    else:
        return-1



li= []
n=int (input ("enter a value"))

for i in range(n):
      li. append (int (input ("enter the value for list:")))
li. sort()
se=int (input ("enter the search element"))
result=(binary_search (0, n-1, li, se))

if(result):
    print(f"Element found at index {result}")
else:
    print("Element found at index")
