def balpar(exp):
    stli=[]
    c=0
    for i in exp:
        if i=='(' or i=='{' or i=='[' or i=='<' :
            stli.append(i)

        elif stli and (i==')' and stli[-1]=='(') or (i=='}' and stli[-1]=='{') or (i==']' and stli[-1]=='[') or (i=='>' and stli[-1]=='<'):
            stli.pop()
            c+=1
            continue
        else:
            #return False
            stli.pop()
    #return True
    print(c)


exp="[{<()>}]"
balpar(exp)

"""k=balpar(exp)

if(k==True):
    print("Balanced ")

else:
    print("Unbalanced")"""

e2="({[>})"
balpar(e2)

"""r=balpar(e2)

if(r==True):
    print("Balanced ")

else:
    print("Unbalanced")"""
