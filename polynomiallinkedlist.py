class Node:
    def __init__(self,coeff,expo):
        self.coeff=coeff
        self.expo=expo
        self.next=None

    def polynomiallist:
        def __init__(self):
            self.head=None
            self.tail=None

        def insert(self,coeff,expo):
            newnode=Node(coeff,expo)
            if self.head is None:
                self.head=newnode
                self.tail=newnode
            else:
                if self.head.expo<expo:
                    newnode.next=self.head
                    self.head=newnode
                elif self.tail.expo>expo:
                    self.tail.next=newnode
                    self.tail=newnode
                else:
                    temp=self.head
                    prev=None
                    while(temp.next!=None and temp.expo>expo):
                        prev=temp
                        temp=temp.next
                    if (temp.expo==expo):
                        temp.coeff+=coeff
                    else:
                        prev.next=newnode
                        newnode.next=temp

        def add(temp1,temp2):
            adobj=polunomiallist()
            while(temp1 and temp2):
                if temp1.expo==temp.expo:
                    adob.insert(temp1.coeff+temp2.coeff ,temp1.expo)
                    temp1=temp1.next
                    temp2=temp2.next
                elif temp1.expo>temp2.expo:
                    adob.insert(temp1.coeff,temp1.expo)
                    temp1=temp1.next
                else:
                    adob.insert(temp2.coeff,temp2.expo)
                    temp2=temp2.next
            while(temp1):
                adob.insert(temp1.coeff,temp2.coeff)
                temp1=temp1.next
            
                    
                    
