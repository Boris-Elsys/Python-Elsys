class triangle:
    a = 0
    b = 0
    c = 0
    
    def __init__(self, a, b ,c):
        self.a = a
        self.b = b
        self.c = c
    
    def circ(self):
        P = self.a + self.b + self.c 
        return P
        
t = triangle(2, 2, 2)
print(t.circ())