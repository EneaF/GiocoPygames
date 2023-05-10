class coda:
    def __init__(self,lista=None):
        if lista==None:
            self.lista=[]
        else:
            self.lista=lista
    
    def push(self,val):
        self.lista.append(val)
    
    def front(self):
        return self.lista[0]
    
    def pop(self):
        self.lista.pop(0)
    
    def empty(self):
        return len(self.lista)==0