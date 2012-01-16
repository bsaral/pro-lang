class Stack:
    def __init__(self):
        self.eleman = []

    def isEmpty(self):
        return self.eleman == []

    def push(self, eleman):
        return self.eleman.append(eleman)
       

    def pop(self):
        return self.eleman.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.eleman)

    def show(self):
        print self.eleman

def baseconverter(binary):
    s=Stack()
    say=0
    for i in binary:
        s.push(int(i))
        say+=1
    sayi=0
    
    for i in range(0,say):
        if not s.isEmpty():
            sayi+=(s.pop()*(2**i))
        else:
            break
    print sayi
        
    

baseconverter("10100")
        

