def linear_search(li, f):
    for j in range (len(li)):
       if f == (li[j]):
           return j
    return False    




li= []
n=int (input ("enter no of values"))
for i in range(n):
      li.append (int (input ("enter the value for list:")))

f=int (input ("enter the search element"))
result= (linear_search(li, f))

if (result):
    print(f"element found at index : {result}")
else:
    print("element not found")
