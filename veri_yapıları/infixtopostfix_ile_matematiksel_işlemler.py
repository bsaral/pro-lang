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
        return self.eleman[len(self.eleman)-1]

    def size(self):
        return len(self.eleman)

    def show(self):
        return self.eleman

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    
    
    for token in tokenList:
        if token.isdigit()==True:
            postfixList.append(int(token))
        elif token == '(':
            opStack.push(token)
            opStack.show()
        elif token == ')':
            opStack.show()
            topToken = opStack.pop()
            
            
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
                
        else:
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    for i in postfixList:
        if type(i)==int:
            opStack.push(int(i))
        else:
            sayi1=opStack.pop()
            sayi2=opStack.pop()
            son=islem(i,sayi1,sayi2)
            opStack.push(son)
    print son

def islem(op,nm1,nm2):
    if op=="*":
        return nm1*nm2
    else:
        if op=="/":
            return nm1/nm2
        else:
            if op=="+":
                return nm1+nm2
            else:
                return nm1-nm2
    
   
        
infixToPostfix("( 5 + 3 ) * 4")










        

