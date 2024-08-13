class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def Insertatend(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head 
        else:
            new_node.next=self.tail.next 
            self.tail.next=new_node
            self.tail=new_node

    def Insertatbegin(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head 

        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next =self.head
    def Insertatposition(self,val,position):
         new_node=Node(val)
         if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head 
         else:
             temp=self.head
             c=0
             while(c<position-1):
                 temp=temp.next
                 c+=1
             new_node.next=temp.next
             temp.next=new_node

    def delete_begin(self):
        if self.head==None:
            print("Linked list doesnot exist")
        else:
            self.head=self.head.next

    def delete_end(self):
        if self.head==None:
            print("Linked list doesnot exist")
        else:
            temp=self.head
            while(temp.next!=self.tail):
                temp=temp.next
            temp.next=self.tail.next
            self.tail=temp

    def delete_pos(self,pos):
        if self.head==None:
            print("Linked list doesnot exist")
        else:
            temp=self.head
            c=0
            while(c<pos-1):
                temp=temp.next
                c+=1
            temp.next=temp.next.next
        
        
                 
    def display(self):
        temp=self.head
        print(temp.value,end="->")
        temp=temp.next
        while(temp!=self.head): 
            print(temp.value,end='->')
            
            temp=temp.next
        print("None")


singley=Linkedlist()
singley.Insertatend(12)
singley.display()

singley.Insertatend(10)
singley.display()

singley.Insertatend(14)
singley.display()

singley.Insertatbegin(19)
singley.display()

singley.Insertatbegin(5)
singley.display()

singley.Insertatposition(8,3)
singley.display()

singley.Insertatposition(9,3)
singley.display()

singley.delete_begin()
singley.display()

singley.delete_end()
singley.display()

singley.delete_pos(3)
singley.display()












