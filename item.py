class Identifier:
    def __init__(self, num, row, col):
        self.num = num
        self.row = row
        self.col = col
        
    def getRow(self):
        return self.row
    def getCol(self):
        return self.col
    def getNum(self):
        return self.num
    
    def setRow(self, r):
        row = r
    def setCol(self, c):
        col = c
    def setNum(self, n):
        num = n
    
stack = []

item = Identifier(8, 3, 2)
item1 = Identifier(9, 5, 2)

stack.append(item)
stack.append(item1)

out1 = stack.pop()
print(out1.num)
print(stack.pop())