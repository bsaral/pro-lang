class Queue:
    def __init__(self,n):
        self.n=n
        self.items = [None]*n
    def isEmpty(self):
        return Queue.isEmpty(self)
    def enq(self, item,sayi):
        self.items.insert(sayi,item)
        if len(self.items)-2>=self.n:
            q.deq()
    def deq(self):
       self.items.pop()
    def size(self):
        return len(self.items)
    def show(self):
        return self.items


q=Queue(3)
q.enq("A",1)
q.enq("B",2)
q.enq("C",2)
q.enq("D",1)
q.show()
