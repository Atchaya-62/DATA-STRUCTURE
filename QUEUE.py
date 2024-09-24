class queue:
    def __init__(self,size):
        self.front=None
        self.rear=None
        self.size=size
        self.qlist=[None]*size

    def isfull(self):
        if self.rear == self.size-1:
            return True
        return False

    def isEmpty(self):
        if self.front==None:
            return True
        return False

    def Enque(self,val):
        if  self.isfull():
            print("Queue is Full")
        else:
            if self.front is None:
                self.front=0
                self.rear=0
                self.qlist[self.rear]=val

            else:
                self.rear=self.rear+1
                self.qlist[self.rear]=val

    def Deque(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            r =self.qlist[self.front]
            if self.front==self.rear:
                self.qlist[self.front]=None
                self.front=None
                self.rear=None
            else:
                self.qlist[self.front]=None
                self.front+=1
            return r

        
    def peak(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.qlist[self.front]


q=queue(int(input("enter size")))
print("1- Enque , 2 - Deque , 3 - peak , 4 - empty , 5- full , 6, exit")
while(1):
    cas=int(input())
    match cas:
        case 1:
            q.Enque(int(input("enter value to be enqueued")))
            print(q.qlist)
        case 2:
            print("Dequed element :",q.Deque())
            print(q.qlist)
        case 3:
            print("Peak element ",q.peak())
        case 4:
            print("Queue is empty :",q.isEmpty())
        case 5:
            print("Queue is full ",q.isfull())
        case 6:
            break

