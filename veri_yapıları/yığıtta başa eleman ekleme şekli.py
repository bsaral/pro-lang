class Stack:
    def __init__(self):
        self.eleman = []

    def isEmpty(self):
        return self.eleman == []

    def push(self, eleman):
        self.eleman.insert(0,eleman)
        print self.eleman

    def pop(self):
        return self.eleman.pop(0)

    def peek(self):
        return self.eleman[0]

    def size(self):
        return len(self.eleman)
