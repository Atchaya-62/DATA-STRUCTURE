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
            self.tail=self.head
           
        else:
           
            self.tail.next=new_node
            self.tail=new_node

    def Insertatbegin(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
            self.tail=self.head

        else:
            new_node.next=self.head
            self.head=new_node

    def Insertatposition(self,val,position):
         new_node=Node(val)
         if self.head is None:
            self.head=new_node
            self.tail=new_node
           
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

    
 
    def search(self,val):
        if self.head is None:
            print("Linked List doesnt exist")
        else:
            temp=self.head
            while(temp):
                if (temp.value==val):
                    print("element found")
                    break
               
                temp=temp.next
            if temp is None:
                print("element not found")
                
    def Reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  
            current.next = prev       
            prev = current           
            current = next_node      
        self.head = prev             
        if self.head:
            self.tail = self.head
            while self.tail.next:
                self.tail = self.tail.next
                 
    def display(self):
        temp=self.head
        
        while(temp!=None):
            print(temp.value,end='->')

            temp=temp.next
        print("None")


singley=Linkedlist()
singley.Insertatend(56)
singley.display()

singley.Insertatend(99)
singley.display()

singley.Insertatend(4)
singley.display()

singley.Insertatbegin(89)
singley.display()

singley.Insertatbegin(53)
singley.display()

singley.Insertatposition(28,3)
singley.display()

singley.Insertatposition(39,3)
singley.display()

singley.search(39)

singley.delete_begin()
singley.display()

singley.delete_end()
singley.display()

singley.delete_pos(3)
singley.display()

singley.search(39)

singley.Reverse()
singley.display()





